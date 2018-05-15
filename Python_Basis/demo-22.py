#对象中存放另一个对象

class Home:
    def __init__(self, new_area, new_addr):
        self.area = new_area
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []
    def __str__(self):
        return "房子的地点： %s, 总面积：%d，可用面积：%d当前房子的物品有：%s"%(self.addr, self.area, self.left_area, str(self.contain_items))
    #将bed1对象添加到fangzi对象中的方法
    def add_item(self, item):
        self.left_area -= item.area
        self.contain_items.append(item.name)

class Bed:
    def __init__(self, new_name, new_area):
        self.area = new_area
        self.name = new_name        
    def __str__(self):
        return "%s占用的面积是：%d"%(self.name, self.area)


fangzi = Home(130, "太原市")
print(fangzi)

bed1 = Bed("席梦思", 4)
print(bed1)

#将bed1对象移到fangzi对象中去
fangzi.add_item(bed1)
print(fangzi)