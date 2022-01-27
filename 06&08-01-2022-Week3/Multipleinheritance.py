class A:
    def __init__(self, name):
        self.name = name
    def greet(self, greeting):
        print("%s -- %s" % (greeting,self.name))
class B:
    def method2(self,org):
        print("%s Miss.%s"% (org,self.name))
class C(A,B):
    def method3(self,wish):
        print("%s %s"%(wish,self.name))

c = C("Elen")
c.greet("Hello")
c.method2("GLad to have ")
c.method3("Welcome")
