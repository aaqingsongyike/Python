#排序

#列表排序
nums = [11,3,4,44555,33,23,654]
nums.sort() #小到大
print(nums)

#字典排序
infos = [
    {"name":"aa","age":12},
    {"name":"dd","age":20},
    {"name":"cc","age":2}
]
infos.sort(key=lambda x:x['name'])
print(infos)
