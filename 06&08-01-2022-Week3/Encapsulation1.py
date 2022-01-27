class Myclass:
    def set_val(self,val):
        self.value = val
    def get_val(self):
        print("Value: ",self.value)
a=Myclass()
b=Myclass()
a.set_val(100)
b.set_val(1000)
a.value=2
a.get_val()
b.get_val()