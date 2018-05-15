#循环语句 while, for，for……else

num = 1
print("while循环")
while num<=10:
    print(num)
    num+=1


print("-"*9)
print("for循环")
name = "杨 郁 彪"
for temp in name:
    print("this is name: %s"%temp)
print("-"*9)


#for 循环之后，执行一次 else
print("for...else")
nums = [11,22,33,44]
for temp in nums:
    print(temp)
else:
    print("========")