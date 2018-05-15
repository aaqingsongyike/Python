#字符串拼接

last_name = "yang"
fitst_name = "yubiao"

name = last_name + fitst_name
print("this is name：%s"%name)
print("="*20)
#字符串常见操作
my_str = "'    my name is yang yu biao AND HE Is student name             '"
Find_l = my_str.find("name")
print("find: %s"%Find_l)  #find返回第一个字符的下标(左到右)

Find_r = my_str.rfind("name")
print("rfind: %s"%Find_r)   #rfind(右到左)

Index = my_str.index("yang")
print("index: %s"%Index)    #index==find

Index_r = my_str.rindex("name")
print("rindex: %s"%Index_r) #rindex==rfind

Count = my_str.count("name")
print("count: %s"%Count)    #count出现次数

Replace = my_str.replace("name", "NAME")    
print("replace: %s"%Replace)    #replace替换全部
Replace_second = my_str.replace("name", "NAME", 1)  #替换一个
print("replace_second: %s"%Replace_second)

Split = my_str.split(" ")
print("split: %s"%Split)    #split按照某个字符切割（空格）

Capitalize = my_str.capitalize()
print("Capitlize: %s"%Capitalize)   #将字符串首字母大写

Title = my_str.title()
print("title: %s"%Title)    #将字符串中的单词首字母全大写

Startwith = my_str.startswith("iji")
print("startwith: %s"%Startwith)    #判断是否是以xxx开头

Endwith = my_str.endswith(".txt")
print("endwith:%s"%Endwith)  #判断是否是以xxx结尾

Lower = my_str.lower()
print("lower: %s"%Lower)    #将所有大写转换成小写

Upper = my_str.upper()
print("upper: %s"%Upper)    #将所有小写转换成大写

Ljust = my_str.ljust(100)
print("ljust: %s"%Ljust)    #返回一个原字符串左对齐并使用空格填充至width的新字符串

Rjust = my_str.rjust(100)
print("rjust: %s"%Rjust)    #返回一个原字符串左对齐并使用空格填充至width的新字符串

Center = my_str.center(50)
print("center: %s"%Center)  #居中

text = "     我是一个学生     "
Lstrip = text.lstrip()
print("lstrip: %s"%Lstrip)  #删除字符串开头的空白字符

Rstrip = text.rsplit()
print("rstrip: %s"%Rstrip)  #删除字符串末尾的空白字符

Strip = text.strip()
print("strip: %s"%Strip)    #删除两端空白字符

str = "yang"
Partition = my_str.partition(str)
print(Partition)    #将字符串以str分为3部分：str前，str，str后

RPartition = my_str.rpartition(str)
print(RPartition)  #(从右开始)

text_one = "hello\nworld\nok"
print("text_one: %s"%text_one)
Splitition = text_one.splitlines()
print("splitlines: %s"%Splitition)       #行分隔

Str_str = "aaa"
if Str_str.isalpha():   #判断是否是字母（强转可以用）
    print("Str_str是字母")
else:
    print("Str_str不是字母")
Num_num = "100"
if Num_num.isdigit():   #判断是否是数字
    print("是数字")
else:
    print("不是数字")
Str_Num = "a10"
if Str_Num.isalnum():   #判断是否是数字和字母的组合
    print("是数字和字母的组合")
else:
    print("不是数字和字母的组合")

Join_a = ["aaa", "bbb", "ccc"]
Join_b = "="
Join = Join_b.join(Join_a)  #连接字符串
print("this is join: %s"%Join)