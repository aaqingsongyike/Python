#多态

class Dog(object):
    def print_self(self):
        print("大家好！我是xxx")

class Dog_XTQ(Dog):
    def print_self(self):
        print("Hello everybody!")

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Dog_XTQ()

introduce(dog1)
introduce(dog2)