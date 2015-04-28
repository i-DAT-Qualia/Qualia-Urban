import multiprocessing

bind = "127.0.0.1:8002"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "tornado"
timeout=90
graceful_timeout=10
