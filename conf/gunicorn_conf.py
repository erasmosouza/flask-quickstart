import multiprocessing


accesslog = "-" # STDOUT
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
bind = "0.0.0.0:8000"
capture_output = True
enable_stdio_inheritance = True
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = "debug" # Valid level names are: debug, info, warning, error, critical
