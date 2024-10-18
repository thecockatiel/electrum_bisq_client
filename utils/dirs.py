import os
import platform
from pathlib import Path

def get_user_data_dir():
    system = platform.system()
    
    if system == "Windows":
        return Path(os.getenv("APPDATA"))

    if system == "Darwin":  # macOS is identified as 'Darwin' in platform module
        return Path(os.path.expanduser("~"), "Library", "Application Support")
    
    # For Unix/Linux systems
    return Path(os.path.expanduser("~"), ".local", "share")

def create_data_dir(app_name):
    data_dir = get_user_data_dir() / app_name
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir
