
import requests
from requests.adapters import HTTPAdapter, Retry
import os
import io
from urllib.parse import urlparse
from tqdm import tqdm
from pathlib import Path
import aiohttp

HTTP_HEADERS = {'User-Agent': 'Electrum-Bisq/1.0'}

def requests_retry_session(
    retries=3,
    backoff_factor=0.6,
    status_forcelist=(500, 502, 504),
    session=None,
) -> requests.Session:
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


async def download_file(url: str, download_dir: Path, skip_if_exists=False):
    download_dir.mkdir(parents=True, exist_ok=True)
    filename: str = os.path.basename(urlparse(url).path)
    download_path = download_dir.joinpath(filename)
    if skip_if_exists and download_path.is_file():
        return download_path

    chunk_size = io.DEFAULT_BUFFER_SIZE
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                total_size = int(response.headers.get("content-length", 0))
                with tqdm(total=total_size, unit="B", unit_scale=True, desc=filename) as progress_bar:
                    response.raise_for_status()
                    with download_path.open('wb') as f:
                        async for chunk in response.content.iter_chunked(chunk_size):
                            if chunk:  # filter out keep-alive new chunks
                                progress_bar.update(len(chunk))
                                f.write(chunk)
                                f.flush()
    except Exception as e:
        download_path.unlink(missing_ok=True)
        raise e
    return download_path
