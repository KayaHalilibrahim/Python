

# def changeName(n):
#     n = 'Ada'
    
    
# name = 'Yiğit'
# changeName(name)   #value
# print(name)



# def change(n):
#     n[0]='İstabul'
    
    
# cities = ['Ankara','İzmir']
# n = cities[:]  #slicing - copy values in cities

# n[0]='istanbul'

# #change(cities) #referance
# change(cities[:]) #does not change

# print(cities)
# print(n)



# def add(*params):
#     print(type(params))
#     print(params[2])
#     # return sum((params))
    
#     sum = 0
#     for n in params:
#            sum += n
           
#     return sum




# print(add(10, 20, 30))
# print(add(10,20,30,50,60))





# def displayUser(**args):   #dictionary
#     print(type(args))
#     for key,value in args.items():
#         print (f'{key} is {value}')


# displayUser(name='Çınar',age=2, city='istanbul')
# displayUser(name='Ada',age=12,city='Kocaeli',phone='5315310')
# displayUser(name ='Yiğit',age=14,city='Ankara',phone='4242412',mail='xx@gmail.com')






def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
        

myFunc(10,20,30,40,50,60,key1='value1',key2='value2')