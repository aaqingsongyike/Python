#生成器————send

def gen():
    i = 0
    while i<5:
        temp =  yield i
        print(temp)
        i+=1
f = gen()
ret = next(f)
f.send("hh")    #hh 取代了 yield i
print(ret)
ret = next(f)
print(ret)
f.send("aa")