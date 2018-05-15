#将信息保存到文件当中
info = []

def load_info():
    global info
    f = open("文件信息保存.txt")
    info = eval(f.read())  #eval将字符串转换成原来的类型
    print(info)
    f.close()


def save_2_file(info):
    f = open("文件信息保存.txt", "w")
    f.write(str(info))  #必须是字符串类型
    f.close()

#加载数据
load_info()

#给文件中添加数据
name = input("please input your name: ")
age = input("please input your age: ")
info = [name, age]
save_2_file(info) #保存到文件中