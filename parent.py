

class Parent: # it's class initialization
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__work = None
        # __work it's a private variable.
        # I can get its value only via function get_work()
        # If I try to get it some other way, I'll get the AttributeError

    def set_work(self, work):
        # I can pass new value for __work variable
        # only via this function
        # __work has a default value as None
        self.__work = work
        return self.__work

    def get_work(self):
        return self.__work


class Child(Parent):
    # It's a child class which inherits from Parent
    # It's the example of Inheritance
    def __init__(self, name, age, hobby, work):
        self.hobby = hobby
        self.work = work

        Parent.__init__(self, name, age)

    def get_work(self):
        # I defined method which has the same name as in the Parent
        # but can get different values. This example of Polymorphism
        if self.work == "housework":
            return self.work
        else:
            self.work = "housework"
            return self.work

