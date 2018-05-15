#导入model-1模块
#import model   #导入方式一

#model.test1()
#from model import test1, test2  #导入方式二
from model import * #导入方式二
import time as tt #给导入包起别名

tt.sleep(3)
test1()
test2()


