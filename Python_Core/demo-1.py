#导入不在当前文件夹下的模块
import sys

sys.path.append("模块路径")

#重新导入模块
from imp import *
reload(test)    #test为需要重新导入的模块