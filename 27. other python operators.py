
# ıdentity operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x==y)  #True  - value
print(x==z)  #True  - value

print (x is y)  #True  - referance
print (x is z)  #False - referance


x = [1,2,3]
y = [2,4]

del x[2]
y[1]=1
y.reverse()
print (F'y:{y} - x:{x}')  

print (f'as value x==y: {x==y}')
print (f'as referance x is y: {x is y}')
print (f'as referance x is not y: {x is not y}')


# Membership Operator: in

x = ['apple', 'banana']
print ('banana' in x)

name = 'Halil'
print ('a' in name)    #True
print ('a' not in name)  #False
