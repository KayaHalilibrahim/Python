

numbers = [1,3,5,7,9,12,19,21]

#1 - Which numbers in the list of numbers are multiples of 3?

for num in numbers:
    if num %3 ==0:
        print(num)
    

#2 - What is the sum of the numbers in the list of numbers?

print()

sum = 0

for s in numbers:
    sum+=s
    
print('sum of the numbers:',sum)



#3 - Square the odd numbers in the list of numbers
print()

for x in numbers:
    if x%2!=0:
        print (f'square of {x}: {x**2}')


cities = ['şanlıurfa','istanbul','ankara','izmir','rize']

#4 - Which of the cities has a maximum of 5 characters?
print()
count = 0

for c in cities:
    if len(c) <= 5:
        print(f'The number of characters in {c} is {len(c)}.')
        

products = [
    {'name':'samsung s6', 'price':'3000'},
    {'name':'samsung s7', 'price':'4000'},
    {'name':'samsung s8', 'price':'5000'},
    {'name':'samsung s9', 'price':'6000'},
    {'name':'samsung s10', 'price':'7000'}
]

#5 - What is sum price of products
print()
sum = 0

for y in products:
    sum += int(y['price']) 
print('sum price of products:',sum)


#6 - Show products with a price of up to 5000
print()
for p in products:
    if int(p['price']) <= 5000:
        print(p['name'])