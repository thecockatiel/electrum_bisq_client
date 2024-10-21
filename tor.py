import threading
import txtorcon
import platform
import os
import re

from electrum.logging import get_logger
from .utils.dirs import create_and_get_tor_dir
from .utils.network import download_file 
import tarfile
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from PyQt6.QtCore import pyqtSignal, QObject
import socket

from typing import TYPE_CHECKING

CURRENT_TOR_VERSION = "13.5.7"

def get_tor_binary_url(version=CURRENT_TOR_VERSION):
    """returns tor binary download url based on the OS and architecture"""
    os_name = platform.system().lower()
    arch = platform.machine()
    x86_64 = ['AMD64', 'x86_64']

    if "arm" in arch:
        raise RuntimeError("ARM architecture is not supported")

    if os_name == "windows":
        if arch in x86_64:
            return f"https://archive.torproject.org/tor-package-archive/torbrowser/{version}/tor-expert-bundle-windows-x86_64-{version}.tar.gz"
        else:
            return f"https://archive.torproject.org/tor-package-archive/torbrowser/{version}/tor-expert-bundle-windows-i686-{version}.tar.gz"
    if os_name == "darwin":
        if arch == "aarch64":
            return f"https://archive.torproject.org/tor-package-archive/torbrowser/{version}/tor-expert-bundle-macos-aarch64-{version}.tar.gz"
        if arch in x86_64:
            return f"https://archive.torproject.org/tor-package-archive/torbrowser/{version}/tor-expert-bundle-macos-x86_64-{version}.tar.gz"

    if os_name == "linux":
        if arch in x86_64:
            return f"https://archive.torproject.org/tor-package-archive/torbrowser/{version}/tor-expert-bundle-linux-x86_64-{version}.tar.gz"
        else:
            return f"https://archive.torproject.org/tor-package-archive/torbrowser/{version}/tor-expert-bundle-linux-i686-{version}.tar.gz"
    
    raise RuntimeError(f"Unsupported OS: {os_name} arch: {arch}")

def get_tor_bin_dir_name(version=CURRENT_TOR_VERSION) -> str:
    name = os.path.basename(get_tor_binary_url(version))
    match = re.match(r'^tor-expert-bundle-\w+-(.*)\.tar\.gz$', name)
    if match:
        return match.group(1)
    else:
        raise RuntimeError(f"Failed to extract tor path from {name}")

def find_tor_in_path():
    """
    Tries to find tor binary in the system PATH and returns the path to the binary. Returns None if not found.
    """
    os_name = platform.system().lower() 
    if os_name != "windows":
        return txtorcon.util.find_tor_binary()
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path_to_try = os.path.join(path, "tor.exe")
            if os.path.isfile(path_to_try):
                return path_to_try
    return None

def find_tor_in_data():
    """
    Tries to find tor binary in app's user data directory Returns None if not found.
    """
    tor_dir = create_and_get_tor_dir()
    os_name = platform.system().lower() 
    expected_bin_dir = tor_dir.joinpath(get_tor_bin_dir_name(), "tor")
    
    if expected_bin_dir.exists():
        if os_name == "windows":
            path = expected_bin_dir.joinpath("tor.exe")
            if path.is_file():
                return path
        else:
            path = expected_bin_dir.joinpath("tor")
            if path.is_file():
                return path

    return None

def download_and_extract_tor():
    """
    Downloads tor binary and extracts it to the app's user data directory.
    """
    tor_bin_url = get_tor_binary_url()
    tor_bin_dir = create_and_get_tor_dir().joinpath(get_tor_bin_dir_name())
    tor_bin_dir.mkdir(parents=True, exist_ok=True)
    
    downloaded_file = download_file(tor_bin_url, skip_if_exists=True)
    archive = tarfile.open(str(downloaded_file))
    archive.extractall(str(tor_bin_dir))
    archive.close()
    
    return find_tor_in_data()

twisted_thread = None
tor: txtorcon.Tor = None

class TorManager(QObject):
    """
    This class manages the tor instance and it's configuration through qt slots and signals.
    """
    proxy_port = pyqtSignal(str)
    having_trouble = pyqtSignal()
    logger = get_logger("bisq tor module")

    def twisted_thread(self):
        # Start the Twisted reactor in the current thread
        reactor.run(installSignalHandlers=False)
        
    async def __setup_tor(self):
        global tor, twisted_thread
        if twisted_thread is None:
            twisted_thread = threading.Thread(target=self.twisted_thread, daemon=True)
            twisted_thread.start()
        if tor == None:
            try:
                with socket.create_connection(("127.0.0.1", "9050"), timeout=5):
                    self.logger.debug("Tor is already running at: 9050. skipping tor launch")
                    self.proxy_port.emit(str(9050))
                    return
            except Exception as e:
                pass
            
            tor_bin_path = find_tor_in_data()

            if tor_bin_path is None:
                tor_bin_path = download_and_extract_tor()
                if tor_bin_path is None:
                    self.having_trouble.emit()
                    return

            tor_data_path = create_and_get_tor_dir().joinpath("data")
            tor_data_path.mkdir(parents=True, exist_ok=True)
            tor_bin_dir = tor_bin_path.parent
            
            tor_config = txtorcon.TorConfig()
            tor_config.AvoidDiskWrites = 1
            tor_config.Log = ["notice stdout"]
            tor_config.DormantCanceledByStartup = 1
            tor_config.DormantOnFirstStartup = 0
            tor_config.ClientTransportPlugin = [
                "meek_lite,obfs2,obfs3,obfs4,scramblesuit,webtunnel exec " + 
                            str(tor_bin_dir.joinpath("pluggable_transports", "lyrebird")) +
                            ".exe\n" if platform.system().lower() == "windows" else "\n",
                "snowflake exec " + 
                            str(tor_bin_dir.joinpath("pluggable_transports", "snowflake-client")) +
                            ".exe\n" if platform.system().lower() == "windows" else "\n",
                "conjure exec " + 
                            str(tor_bin_dir.joinpath("pluggable_transports", "conjure-client")) +
                            ".exe\n" if platform.system().lower() == "windows" else "\n"
            ]
            tor_config.GeoIPFile = str(tor_bin_dir.parent.joinpath("data", "geoip"))
            tor_config.GeoIPv6File = str(tor_bin_dir.parent.joinpath("data", "geoip6"))

            # read "bridges" file from tor_data_path directory and add it to tor_config
            bridges_file = tor_data_path.joinpath("bridges")
            if bridges_file.exists():
                try:
                    with open(bridges_file, "r") as f:
                        tor_config.UseBridges = 1
                        bridges = f.read().splitlines()
                        tor_config.Bridge = bridges
                except Exception as e:
                    self.logger.error(f"Failed to read bridges file: {e}")


            # write config as log for debugging purposes
            with open(tor_data_path.joinpath("torrc.log"), "w") as f:
                f.write(tor_config.create_torrc())


            tor = await txtorcon.launch(reactor, progress_updates=self.logger.info,
                            tor_binary=str(tor_bin_path),
                            data_directory=str(tor_data_path),
                            kill_on_stderr=True,
                            _tor_config=tor_config)
        socks_port = await tor.protocol.get_conf("SOCKSPort")
        self.proxy_port.emit(str(socks_port))
    
    def setup_tor(self):
        d = Deferred.fromCoroutine(self.__setup_tor())
        d.addErrback(lambda _: self.having_trouble.emit())
        return d
