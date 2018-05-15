# if、 if……else、 if……elif、  类型转换

age = input("请输入您的年龄：")

age_num = int(age)  #类型转换(Str--->int)

if age_num>=18:
    print("this is age: %d"%age_num)
    print("你可以去网吧！！！")
else:
    print("你不可以去网吧！！！")
print("你的年龄是：%d"%age_num)
print("="*10)
String = 100
String_a = str(String)  #(int---->Str)
print("this is String_a%s"%String_a)

print("-"*9)
##########################################
num = 100
if num==10:
    print("num==10")
elif num==100:
    print("num==100")
elif num==20:
    print("num==100")
else:
    print("num等于50")





