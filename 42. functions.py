

#function  --They are not defined inside the class.

# def sayHello(name='user'):
#     print('Hello '+ name)
    
    
    

# sayHello('Halil')
# sayHello('Ada')
# sayHello()


# def sayHello(name='user'):
#    return 'Hello '+ name
    
    
    

# print(sayHello('Halil'))
# print(sayHello('Ada'))
# print(sayHello())




# def total(num1,num2):
#     return num1+num2

# result = total(10,60)
# print(result)


def ageCalculation(birtdate):
    return 2024-birtdate




myAge = ageCalculation(2002)
#print(myAge)   



def retirmnt(birthdate, name):
    
    '''
    DOCSTRING:How many years until retirement based on your birth year.
    Input: Birth Year, name 
    Output: Calculated year
    '''
    
    age = ageCalculation(birthdate)
    retirement = 65 - age
    
    if retirement>0:
        print (f'You have {retirement} years left until retirement.')

    else:
        print('You are a retirement.')



retirmnt (2002,'ibrahim')
retirmnt (1950,'Murat')


print(help(retirmnt))  #it print comment inside of function.
print(help(list.append))