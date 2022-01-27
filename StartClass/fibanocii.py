'''Generate the fibanocii series upto 100
n1=0
n2=1
def fibanocii(n):
    for n in range(1,n+1):

n=int(input('Enter a number: '))
print('Fibanocii series: ',n1,n2)'''

def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ');
        num1 = num2;
        num2 = series;
        series = num1 + num2;
num = int(input('Enter how many numbers needed in Fibonacci series- '))
fibonacci(num)




