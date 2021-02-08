import logging
import subprocess
from inference.environment import HostEnvironment

env = HostEnvironment()
logger = logging.getLogger(__name__)


def _launch_gunicorn():
    
    """Configure and launch the Gunicorn web server 
    """
    
    gunicorn_bind_address = '0.0.0.0:8080'

    logger.info("starting gunicorn")
    gunicorn_pid = subprocess.Popen(["gunicorn",
                                        "--timeout", str(env.server_worker_timeout),
                                        "-k", "gevent",
                                        "-b", gunicorn_bind_address,
                                        "--worker-connections", str(1000 * env.server_worker_num),
                                        "-w", str(env.server_worker_num),
                                        "inference.wsgi:app"]).pid
    return gunicorn_pid


def startInference():
    gunicorn_pid = _launch_gunicorn()


if __name__ == '__main__':
    try:
        startInference()
    except Exception as e:
        logger.error(e)