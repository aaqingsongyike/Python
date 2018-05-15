
# break、    continue

print("break")  #结束本次循环
i = 1
num = 0
while i<=100:
    if i%2==0:
        print("偶数为：%d"%i)
        num+=1
    
    if num==10:
        break
    i+=1

print("="*9)
print("continue")   #结束当前条件继续循环
num_a = 0
while num_a<10:
    num_a+=1
    print("-"*3)
    if num_a == 3:
        continue
    print(num_a)
