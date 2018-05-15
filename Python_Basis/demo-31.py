#实例方法、类方法、静态方法

class Game(object):
    #类属性
    num = 0

    #实例方法
    def __init__(self):
        self.name = "dota2" #实例属性

    #类方法(可以对类属性进行操作)
    @classmethod
    def add_num(cls):
        cls.num = 100

    #静态方法(和类、实例没有关系，只完成基本操作)
    @staticmethod
    def print_menu():
        print("-"*20)
        print("菜单1")
        print("菜单2")
        print("菜单3")
        print("-"*20)


game = Game()
#Game.add_num()  #调用类方法一
game.add_num()  #调用类方法二
print(Game.num)

#game.print_menu() #调用静态方法一
Game.print_menu() #调用静态方法二