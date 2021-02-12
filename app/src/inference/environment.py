import os
import logging

class HostEnvironment():
    """Provides access to common aspects of the container environment, including
    important system characteristics, filesystem locations, and configuration settings.
    """

    BASE_DIRECTORY = "/opt/ml"
    GUNICORN_SERVER_WORKER_TIMEOUT = "GUNICORN_SERVER_WORKER_TIMEOUT"
    GUNICORN_SERVER_WORKER_NUM = "GUNICORN_SERVER_WORKER_NUM"
    LOG_LEVEL = "LOG_LEVEL"

    def __init__(self):
        self.server_worker_timeout = os.environ.get("GUNICORN_SERVER_WORKER_TIMEOUT", 60)
        self.server_worker_num = os.environ.get("GUNICORN_SERVER_WORKER_NUM", 1)

        # Set the log level
        self.log_level = os.environ.get("LOG_LEVEL", 20)


def configure_logging():
    
    env = HostEnvironment()

    if env.log_level == 10:
        default_level = logging.DEBUG
    elif env.log_level == 20:
        default_level = logging.INFO
    elif env.log_level == 30:
        default_level = logging.WARN
    else:
        default_level = logging.ERROR

    logging.basicConfig(format=format, level=default_level)
    logging.getLogger("demo").setLevel(default_level)