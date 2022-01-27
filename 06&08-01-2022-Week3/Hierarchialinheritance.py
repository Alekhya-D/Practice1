class A:
    def __init__(self, name):
        self.name = name
    def eat(self,item):
        print("%s -- %s"%(self.name, item))
class B(A):
    def fetch(self,thing):
        print("%s goes behind the %s"%(self.name,thing))
class C(A):
    def swat(self):
        print("%s swat the string" %(self.name))

d = B("Bam")
c = C("ninyo")
c.swat()
d.fetch("disc")
c.eat("Milk")