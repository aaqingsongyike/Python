import urllib.request

test = "test"
passworld = "123456"
webserver = "192.168.21.52"

# 构建一个密码管理对象，用来保存和HTTP请求相关的授权账户信息
passworldMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息，参数1：一般为None，其余分别为IP，用户名，密码
passworldMgr.add_password(None, webserver, test, passworld)

# HTTP基础验证处理器
httpauth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr=passworldMgr)

opener = urllib.request.build_opener(httpauth_handler)

request = urllib.request.Request("http://"+webserver)

response = opener.open(request)
print(response.read())