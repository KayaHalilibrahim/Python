

# numbers = [1,3,5,7,9,12,19,21]


# #1Print the list of numbers to the screen with while.
# i = 0
# while i<len(numbers):
#     print(numbers[i])
#     i+=1
    
    
# #2Get the starting and ending values ​​from the user and print all the odd numbers to the screen.
# print()

# f = int(input('Enter first number:'))
# e = int(input('Enter last number: '))

# i=f
# while i<e:
#     print(i)
#     i +=1


# #3 Print the numbers between 1-100 in decreasing order.

# print()

# i = 100
# while i!=1:
#     print(i)
#     i -=1

#4 Print the 5 numbers you will get from the user in order on the screen.
# num =[]

# while len (num) !=5:
#     n = int(input())
#     num.append(n)
# num.sort()
# print(num)

#5 Store the unlimited product information you will get from the user in the product list.
print()
count = int(input('How many products do you want to add:'))

i= 0
products = {}
while i<count:
    name = input('product name: ')
    price = int (input('price: '))
    products[name] =price
    i +=1

print (products)

    #Ask the user for the number of products
    #Make a dictionary list and let it be in the form of (name, price)
    #When the product adding process is finished, list the products on the screen with while