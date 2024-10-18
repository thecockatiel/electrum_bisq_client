import os
import platform
from pathlib import Path

app_name = "bisq_light"

def get_user_data_dir():
    system = platform.system()
    
    if system == "Windows":
        return Path(os.getenv("APPDATA"))

    if system == "Darwin":  # macOS is identified as 'Darwin' in platform module
        return Path(os.path.expanduser("~"), "Library", "Application Support")
    
    # For Unix/Linux systems
    return Path(os.path.expanduser("~"), ".local", "share")

def create_and_get_data_dir():
    path = get_user_data_dir().joinpath(app_name) 
    path.mkdir(parents=True, exist_ok=True)
    return path

def create_and_get_download_dir():
    path = get_user_data_dir().joinpath(app_name, "downloads")
    path.mkdir(parents=True, exist_ok=True)
    return path

def create_and_get_tor_dir():
    path = get_user_data_dir().joinpath(app_name, "tor")
    path.mkdir(parents=True, exist_ok=True)
    return path
