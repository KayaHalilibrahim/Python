
# print number from 1 to 100

x = 1

# while x<=100:
#     print(x)
#     x += 1


# while x<=100:
#     if x%2==0:
#         print(x)
#     x += 1


name = '' # False

print(bool(name))

while not name.strip():    #True -- name.strip(): To remove characters from name.strip() .
    name = input('Enter your name: ')

print('Hello',name)