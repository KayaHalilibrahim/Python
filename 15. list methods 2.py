
numbers = [1,40,58,9,10,3]
letters = ['a','f','g','a','k','c','p']

val = min(numbers)
print (val)
val =  max(numbers)
print (val)

val = min (letters)
print (val)
val = max(letters)
print(val)

val = numbers[3:6]
print (val)

val = numbers[::-1]
print (val)


numbers.append(90)
print (numbers)

numbers.insert(5,70)
print (numbers)

numbers.insert(-1,100)
print (numbers)

print(numbers.pop())  # numbers.pop(-1)
print(numbers)

numbers.pop(2)
print(numbers)

numbers.remove(3) # here 3 not index, it is element
print (numbers)

numbers.sort()
print (numbers)

letters.sort()
print (letters)

numbers.reverse()
print(numbers)


letters.reverse()
print (letters)

print (numbers.count(10)) # How many 10s are there?

print (letters.count('a'))


numbers.clear()
print (numbers)