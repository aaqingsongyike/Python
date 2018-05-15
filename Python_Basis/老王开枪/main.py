#老王开枪

class Person(object):
    '''人的类'''
    def __init__(self, name):
        self.name = name

    def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
        '''把子弹安装到弹夹中'''
        dan_jia_temp.baocun_zidan(zi_dan_temp)
        

class Gun(object):
    '''枪类'''
    def __init__(self, name):
        self.name = name    #枪类型

class Danjia(object):
    '''弹夹类'''
    def __init__(self, max_num):
        self.max_num = max_num    #容量
        self.zidan_liset = []   #记录所有子弹的引用
    def baocun_zidan(self, zi_dan_temp):
        '''将子弹保存'''
        self.zidan_liset.append(zi_dan_temp)

class Zidan(object):
    '''子弹类'''
    def __init__(self, sha_shang_li):
        self.sha_shang_li = sha_shang_li    #杀伤力

def main():
    '''用来控制整个程序的流程'''
    #1创建一个老王对象
    laowang = Person("老王")

    #创建一个枪对象
    ak47 = Gun("AK47")

    #创建一个弹夹对象
    dan_jia = Danjia(20)
    #创建一些子弹
    zi_dan = Zidan(10)
    #创建敌人对象

    #老王把子弹安装到弹夹中
    laowang.anzhuang_zidan(dan_jia, zi_dan)
    #老王把子弹装到枪中

    #老王拿枪

    #老王开枪打敌人


if __name__ == '__main__':
    main()
