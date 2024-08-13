
#1 - Write a function that displays a given word on the screen a specified number of times.

# def write(name,x):
#    print(name*x)
   
    
# write('Halil\n', 5)



#2 - Write a function that converts an unlimited number of parameters sent to it into a list.

# def convertList(*params):
#     myList=[]
#     for n in params:
#         myList.append(n)

#     return myList




# result = convertList(1,2,3,'Halil')
#print (result)

#3 - Find all prime numbers between two numbers sent.


# def primeNumber(num1,num2):
#     for num in range(num1, num2 + 1):
#         if num > 1:
#             for i in range(2,num):
#                 if num % i ==0:
#                     break
#             else:
#                 print(num)
                
                

# primeNumber(5,15)
        
        






#4 - Write a function that returns a list of the exact divisors of a number sent to it.

def divList(number):
    divisorList =[]
    for i in range(1,number+1):
        if number % i ==0:
            divisorList.append(i)

    return divisorList


result = divList(50)
print(result)
