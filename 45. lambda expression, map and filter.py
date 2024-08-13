

# def  square (num):return num **3



# numbers = [1,3,4,8]

# #map listedeki elemanları tek tek gönderir.

# result= list(map (square,numbers))



# for item in map (square,numbers):
#     print(item)


# print(result)


#--------------------------------------------


# square = lambda num: num**2

# numbers = [1,3,4,8]

# # result = list(map(lambda num: num**2,numbers))
# result = list(map(square,numbers))
    
# print(result)


# result2 = square(3)
# print(result2)


#--------------------------------------------
numbers2 = [1,3,4,8,10]

# def checkEven(num): return num%2==0

check_even = lambda num: num%2==0


#result = list (filter(checkEven,numbers2))
#result = list (filter(lambda num: num%2==0,numbers2))
result = list (filter(check_even,numbers2))
result2 = check_even(numbers2[2])

print(result)
print(result2)


