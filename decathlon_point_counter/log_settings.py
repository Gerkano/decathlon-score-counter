import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='logs.log',
    filemode='w'
)
def debug_log(message: str):
    logging.debug(message)

def info_log(message: str):
    logging.info(message)

def warning_log(message: str):
    logging.warning(message)

def error_log(message: str):
    logging.error(message)

def critical_log(message: str):
    logging.critical(message)