'''write a python prog to calculate the factorial of a given number'''
i=1
n=1
k=int(input('Enter a number to find its factorial:'))
for i in range(1,k+1):
    n=i*n;
print('Factorial of a given number is: ',n)


