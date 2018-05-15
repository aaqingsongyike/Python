#保护（隐藏）对象的属性

class Dog:
    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age
        else:
            self.age = 0
    def get_age(self):
        return self.age

dog = Dog()
dog.set_age(10)
age = dog.get_age()
print(age)