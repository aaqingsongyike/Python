#数组下标

name = "yangyubiao"
print("this is name[3]: %s"%name[3])    #从左往右取
print("this is name[-1]: %s"%name[-1])  #从右往左取
print("="*20)

#切片
Name = "YangYuBiaoA"
print("this is Name[4:6]:%s"%Name[4:6])
print("this is Name[4:-1]:%s"%Name[4:-1])
print("this is Name[4:]:%s"%Name[4:])
print("this is Name[4:-1:2]:%s"%Name[4:-1:2])   #间隔取
print("this is Name[-1::-1]:%s"%Name[-1::-1]) #逆序取