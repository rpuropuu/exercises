class Cat:
    breed = "pers"
    def hello(*args):
        print("Hello, World!)", args)


    def show_breed(self):
        print(f"my breed is {self.breed}")


    def show_name(self):
        if hasattr(self, "name"):
            print(f"my name is {self.name}")
        else:
            print("Nothing")


    def set_value(self, value, age=0):
        self.name = value
        self.age = age
