class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self,item):
        print("%s -- %s"%(self.name, item))
class dog(Animal):
    def fetch(self,thing):
        print("%s goes behind the %s"%(self.name,thing))
class cat(Animal):
    def swat(self):
        print("%s swat the string" %(self.name))

d = dog("Bam")
c = cat("ninyo")
c.swat()
d.fetch("disc")
c.eat("Milk")
