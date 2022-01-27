class My_ABC_Class(object):
    def set_val(self,val):
        return
    def get_val(self):
        return
class MyClass(My_ABC_Class):
    def set_val(self,input):
        self.val = input
    def hello(self):
        print("\ncalling the hello() method")
        print("I'm *not* part of the abstract method that is part of My_ABC_Class()")
my_class = MyClass()
my_class.set_val(10)
print(my_class.get_val())
my_class.hello()
