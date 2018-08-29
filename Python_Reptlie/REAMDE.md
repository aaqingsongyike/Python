demo-01:
    urllib.request
demo-02:
    request = urllib.request.Request("http://www.baidu.com", headers=ua_headers)
    重构 response = urllib.request.urlopen(request)
    返回http的响应码response.getcode() 200表示正常，4服务器页面出错，5服务器问题
                                            用于判断是否请求成功
    返回实际数据的URL防止重定向 response.geturl()
    返回http响应的报头 response.getinfo()
demo-03:
    add_hearder()方法，添加/修改一个Http报头
    get_header()方法，获取一个已有的Http报头的值，注意第一个字母大写，其余小写
demo-04:
    关键字编码与解码
    编码 urllib.parse.urlencode(wd).encode('utf-8')
    解码 urllib.parse.unquote(values)
demo-05:
    爬取贴吧练习
demo-06:
    GET请求和POST请求的区别：
        GET请求会附带查询参数
        POST请求不会附带参数
    POST
demo-07:
    ajax请求
demo-08:
    模拟Cookie登录
demo-09:
    HTTPS请求
demo-10:
    Handler和Opener以及开发代理和私密代理的使用
        通过相关的Handler处理器构造处理器对象，支持某些特定的功能
        构建自定义的opener对象，调用open方法发送请求
    代理和私密代理
demo-11:
    代理和web客户端授权验证处理的使用
        HTTPPassworldMgrWithDefaultRealm()
        这个类会创建一个密码管理对象，用来保存和HTTP相关的授权信息
            1.ProxyBasicAuthHandler() 授权代理处理器
            2.HTTPBasicAuthHandeler() 验证web客户端的授权处理器
demo-12:
    Cookie
demo-13:
    使用正则爬虫
demo-14:
    lxml库
demo-15：
    bs4库
demo-16:
    json
demo-17:
    多线程爬虫