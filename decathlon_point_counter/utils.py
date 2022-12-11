import os
from werkzeug.utils import secure_filename
import log_settings

def get_file_location(upload_folder: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), upload_folder)

def save_file(file, upload_folder: str) -> None:
    filename = secure_filename(file.filename)
    file.save(os.path.join(get_file_location(upload_folder), filename))

def convert_timestamp_to_float(timestamp_result: str) -> float:
    time_list = timestamp_result.split(".")
    converted = float(time_list[0])*60 + float(".".join([time_list[1], time_list[2]]))
    log_settings.info_log(f"Timestamp: {timestamp_result}, converted to seconds: {converted}")
    return converted
