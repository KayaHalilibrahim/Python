

X = 5

y = 10

z =20

x, y, z = 5,16,20

#x,y = y,X


x+= 5 # x = x+5   -> 10
x-= 5 # x = x-5   ->5
x*= 5 # x = x*5   ->25
x/= 5 # x = x/5   ->5
x%= 5 # x = x%5   ->0
y//=5 # x= x//5   ->1
y**=5 # y= y**5   ->243

# print (x,y,z)

values = 1,2,3
print (values)
print (type(values))


x,y,z = values
print(x,y,z)

values = 1,2,3,4,5
x,y,*z = values
print(x,y,z)   # 1 2 [3, 4, 5]
print (z[0])

 
 