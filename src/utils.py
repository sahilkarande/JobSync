import os

def create_directory(path: str):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def is_valid_file(file_path: str) -> bool:
    """Checks if the provided file path is valid."""
    return os.path.isfile(file_path)

def format_date(date_string: str, current_format: str, desired_format: str) -> str:
    """Formats a date from one format to another."""
    from datetime import datetime
    try:
        return datetime.strptime(date_string, current_format).strftime(desired_format)
    except ValueError:
        return None

def log_message(message: str, level: str = "INFO"):
    """Logs a message with a specific level."""
    levels = ["INFO", "WARNING", "ERROR"]
    if level not in levels:
        raise ValueError("Invalid log level")
    print(f"[{level}] {message}")
