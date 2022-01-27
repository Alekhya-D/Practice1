class person:
    name="I hahve no name :("
    def selfName(self):
        print('Name: ',self.name)

    def __init__(self, aName):
        self.name = aName

def main():
    #aPerson = person()
   # aPerson.selfName()
    #aPerson = person("Harry")
    #print('Name: ',aPerson.name)
    aPerson = person()
    print('Name: ', aPerson.name)

main()