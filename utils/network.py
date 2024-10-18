
import requests
from requests.adapters import HTTPAdapter, Retry
import os
import io
from urllib.parse import urlparse
from .dirs import create_and_get_download_dir
from tqdm import tqdm

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


def download_file(url, skip_if_exists=False):
    filename: str = os.path.basename(urlparse(url).path)
    download_path = create_and_get_download_dir().joinpath(filename)
    if skip_if_exists and download_path.is_file():
        return download_path
    r = requests_retry_session().get(
        url, stream=True, allow_redirects=True, headers=HTTP_HEADERS
    )
    r.raise_for_status()
    total_size = int(r.headers.get("content-length", 0))
    buffer_size = io.DEFAULT_BUFFER_SIZE
    with tqdm(total=total_size, unit="B", unit_scale=True, desc=filename) as progress_bar:
        with download_path.open('wb') as f:
            for chunk in r.iter_content(chunk_size=buffer_size):
                if chunk:  # filter out keep-alive new chunks
                    progress_bar.update(len(chunk))
                    f.write(chunk)
                    f.flush()
    return download_path
