
#1

cars = ['Bmw','mercedes','Opel','Mazda']
print (len(cars))

#2
print ('first: ',cars[0], 'last: ' , cars[-1])

#3
cars[3] ='Toyota'
print (cars)

#4
print ('mercedes' in cars) # checks if it is on the list.

#5
print (cars[-2])

#6
result = cars[0:3] #car[0],cars[1],cars[2]
print (result)

#7
cars[-2:] = ['Toyota','Renault']
print (cars)

#8
cars.append('Audi')
cars.append('Nissan')
print(cars)           # result = cars + ['Audi','Nissan']

#8
del cars[-1]
print (cars)

#9
print (cars[::-1])


#10
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]


#11
result= f'Y{studentA[0]} {studentA[1]} {2024- studentA[2]} yaşında ve not ortalaması {round(((studentA[3][0]+studentA[3][1]+studentA[3][2])/3),2)}'
print (result)





