fruits = {'orange', 'apple', 'banana'}

print (fruits)

# for x in fruits:
#     print(x)
    
    

fruits.add('Cherry')
fruits.update(['mango','grape','apple'])   # we cannot add the same element.
     
print(fruits)

myList = [1,2,3,1,4,4,5]
print(myList)

print(set(myList))


fruits.remove('mango')  # fruits.discard() , fruits.pop()
print(fruits)

fruits.clear()
print(fruits)