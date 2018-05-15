#类属性-实例属性

class Tool(object):
    #类属性
    num = 0 #类属性

    #方法
    def __init__(self, new_name):
        self.name = new_name    #实例属性
        #对类属性操作
        Tool.num+=1

tool1 = Tool("铁锹")
tool2 = Tool("铲子")
tool3 = Tool("水桶")
print(Tool.num)