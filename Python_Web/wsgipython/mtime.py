import time

def application(env, statusHandle):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    statusHandle(status, headers)
    return time.ctime()