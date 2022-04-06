from parent import Child


class SecondChild(Child):
    def __init__(self, name, age, hobby, work):
        Child.__init__(self, name, age, hobby, work)

    def get_work(self):
        if self.work != "homework":
            self.work = "homework"
            return self.work
        else:
            return self.work

