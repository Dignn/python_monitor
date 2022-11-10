import time
from threading import Thread

from prometheus_client import start_http_server, Counter

run_time = Counter("run_time", "monitor the running time of program")


def run_time_incr():
    while 1:
        run_time.inc()
        time.sleep(1)


def run_http_server(port):
    run_time_thread = Thread(target=run_time_incr)
    run_time_thread.daemon = True
    run_time_thread.start()
    start_http_server(port)

