
import os
import datetime
import logging
import sys
import time

PROC_NAME = os.path.basename( sys.argv[0] )
logger = logging.getLogger( PROC_NAME )

def configure_logging(console_log_level=logging.INFO,
                      console_log_format=None,
                      file_log_path=None,
                      file_log_level=logging.INFO,
                      file_log_format=None,
                      clear_handlers=False):
    """Setup logging.

    This configures either a console handler, a file handler, or both and
    adds them to the root logger.
    Args:
        console_log_level (logging level): logging level for console logger
        console_log_format (str): log format string for console logger
        file_log_path (str): full filepath for file logger output
        file_log_level (logging level): logging level for file logger
        file_log_format (str): log format string for file logger
        clear_handlers (bool): clear existing handlers from the root logger

    Note:
        A logging level of `None` will disable the handler.
    """
    if file_log_format is None:
        file_log_format = \
            '%(asctime)s|%(levelname)-7s|(%(name)s)|%(message)s'

    if console_log_format is None:
        console_log_format = \
            '%(asctime)s|%(levelname)-7s|(%(name)s)|%(message)s'

    # configure root logger level
    root_logger = logging.getLogger()
    root_level = root_logger.level
    if console_log_level is not None:
        root_level = min(console_log_level, root_level)
    if file_log_level is not None:
        root_level = min(file_log_level, root_level)
    root_logger.setLevel(root_level)

    # clear existing handlers
    if clear_handlers and len(root_logger.handlers) > 0:
        for handler in root_logger.handlers:
            root_logger.removeHandler(handler)

    # file logger
    if file_log_path is not None and file_log_level is not None:
        log_dir = os.path.dirname(os.path.abspath(file_log_path))
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        file_handler = logging.FileHandler(file_log_path)
        file_handler.setLevel(file_log_level)
        file_handler.setFormatter(logging.Formatter(file_log_format))
        root_logger.addHandler(file_handler)

    # console logger
    if console_log_level is not None:
        #mod by yk 20171107
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_log_level)
        console_handler.setFormatter(logging.Formatter(console_log_format))
        root_logger.addHandler(console_handler)
