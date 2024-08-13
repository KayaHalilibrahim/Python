

# range()

# list = [1,2,3]

# for item in range(10):  # print from 0 to 9
#     print(item)
    
    
    
# print()
    
# for item in range(2,10):  # print from 2 to 9
#     print(item)
    
# print()

# for item in range(20,100,10):  # print from 20 to 100 step is 10
#     print(item)
    

# print (list(range(20,100,10)))



#enumarate()


# index = 0
# greeting = 'Hello'

# for letter in greeting:
#     print(f'index: {index} - letter: {greeting[index]}')
#     index +=1


# greeting = 'Hello'

# for index,letter in enumerate(greeting):
#     print(f'index: {index} - letter: {greeting[index]}')



#zip()

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]


print (list(zip(list1,list2,list3)))


for item in zip (list1,list2,list3):
    print(item)
    
    
for a,b,c in zip (list1, list2,list3):
    print(a,b,c)





