import asyncio
from typing import (NamedTuple, Callable, Optional, TYPE_CHECKING)

import queue
import sys
from PyQt6.QtCore import (pyqtSignal, QThread)
from electrum.logging import Logger, get_logger
from electrum.util import get_asyncio_loop
from twisted.internet.defer import Deferred

if TYPE_CHECKING:
    from PyQt6.QtCore import QObject


# Copied from electrum desktop. todo: remove once it is moved into a common place in electrum between qml and qt
class TaskThread(QThread, Logger):
    '''Thread that runs background tasks.  Callbacks are guaranteed
    to happen in the context of its parent.'''

    class Task(NamedTuple):
        task: Callable
        cb_success: Optional[Callable]
        cb_done: Optional[Callable]
        cb_error: Optional[Callable]
        cancel: Optional[Callable] = None

    doneSig = pyqtSignal(object, object, object)

    def __init__(self, parent, on_error=None):
        QThread.__init__(self, parent)
        Logger.__init__(self)
        self.on_error = on_error
        self.tasks = queue.Queue()
        self._cur_task = None  # type: Optional[TaskThread.Task]
        self._stopping = False
        self.doneSig.connect(self.on_done)
        self.start()

    def add(self, task, on_success=None, on_done=None, on_error=None, *, cancel=None):
        if self._stopping:
            self.logger.warning(f"stopping or already stopped but tried to add new task.")
            return
        on_error = on_error or self.on_error
        task_ = TaskThread.Task(task, on_success, on_done, on_error, cancel=cancel)
        self.tasks.put(task_)

    def run(self):
        while True:
            if self._stopping:
                break
            task = self.tasks.get()  # type: TaskThread.Task
            self._cur_task = task
            if not task or self._stopping:
                break
            try:
                result = task.task()
                self.doneSig.emit(result, task.cb_done, task.cb_success)
            except BaseException:
                self.doneSig.emit(sys.exc_info(), task.cb_done, task.cb_error)

    def on_done(self, result, cb_done, cb_result):
        # This runs in the parent's thread.
        if cb_done:
            cb_done()
        if cb_result:
            cb_result(result)

    def stop(self):
        self._stopping = True
        # try to cancel currently running task now.
        # if the task does not implement "cancel", we will have to wait until it finishes.
        task = self._cur_task
        if task and task.cancel:
            task.cancel()
        # cancel the remaining tasks in the queue
        while True:
            try:
                task = self.tasks.get_nowait()
            except queue.Empty:
                break
            if task and task.cancel:
                task.cancel()
        self.tasks.put(None)  # in case the thread is still waiting on the queue
        self.exit()
        self.wait()

logger = get_logger("aio")
def run_asyncio_task(coroutine, parent: 'QObject'):
    global logger
    thread = TaskThread(parent)
    fut = asyncio.run_coroutine_threadsafe(coroutine, get_asyncio_loop())
    d = Deferred()
    def on_done(*args, **kwargs):
        try:
            if d.called:
                return
            d.callback(fut.result())
        except Exception as e:
            logger.error(e)
            d.errback()
    def on_error(*args, **kwargs):
        if d.called:
            return
        d.errback()
    thread.add(
        fut.result,
        on_success=on_done,
        on_error=on_error,
        on_done=on_done,
        cancel=fut.cancel,
    )
    return d