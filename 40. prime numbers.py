

number = int(input('Please enter a number: '))

isPrime = True

if (number==1):
    isPrime = False



for i in range (2,number):
    if(number%i==0):
        isPrime=False
        break
    
if isPrime:
    print('This number is prime number')
else:
    print('This number is not prime number') 
    
    
    