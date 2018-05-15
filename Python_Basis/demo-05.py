#逻辑运算

#或  or
you = input("你去吗？")
you_wife = input("你老婆去吗？")
if you == "去" or you_wife == "去":
    print("OK")
else:
    print("NO")

#并且 and
you_son = input("你儿子去吗？")
son_wife = input("儿媳去吗？")
if you_son == "去" and son_wife == "去":
    print("OK")
else:
    print("NO")

#取反 not
num = 90
print("num的值是：%d"%num)
if not(num>0 and num<50):
    print("num不在0~50之间")
else:
    print("num在0~50之间")