class A:
    def __init__(self,name):
        self.name=name
class B(A):
    def mrng(self,day):
        print("%s %s"%(self.name,day))
class C(B):
    def night(self,nite):
        print("%s %s"%(self.name,nite))
c = C("Sri ")

c.mrng("Good morning")
c.night("Good night")
