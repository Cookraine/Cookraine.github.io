class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

    def say_bye(self):
        print('Goodbye!')


p = Person('Dmytro')
h = Person('Oleh')
p.say_hi()
h.say_hi()
p.say_bye()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()