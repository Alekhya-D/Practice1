#import statements can be done in three ways for functions in differents modules
'''
from <file name> import <func name> -- we can use this if we know the functions that we are importing
from <file name> import *  -- we can use this to import all the functions available in that module
import <file name>  --  we can import the file name and call the function using filename.funcname()
'''
#import statement can be done in the following way for importing functions from class
'''
from <filename> import <classname>
'''
from file1 import fun1,fun2
import file2
from Greetings import Greetings  #classname should be matched with the filename
def main():
    fun1()
    fun2()
    file2.fun3()
    a = Greetings()  #creating instance for the class to use it using instance
    a.sayGreeting()     #calling sayGreetings() method from Greetings class using instance
main()