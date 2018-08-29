def application(env, statusHandle):
    print("not")
    status = "404 Not Found"
    print(status)
    headers = []
    statusHandle(status, headers)
    print("abc")
    return "file not found"