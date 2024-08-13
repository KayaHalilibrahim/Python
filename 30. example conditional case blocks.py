
#1
# name = input('Name: ')
# age = int(input('Age: '))
# education = input('Education Information: ')

# if age >=18:
#     if education =='high school' or education=='university':
#         print("You can get a driver's license")
#     else:
#         print('You must be a high school or university graduate.')
# else:
#     print('You are under 18 years old.')
  
  
    
#2
# midterm1 = int(input('midterm 1: '))
# midterm2 = int(input('midterm 2: '))
# finalexam = int(input('final: '))

# average = (midterm1+midterm2+finalexam)/3

# print ("Your average: {}",format(round(average,2)))

# if(average<24):
#     print('Your grade: 0')
    
# elif(average>=24 and average<=44):
#     print('Your grade: 1')
    
# elif(average>=45 and average<=54):
#     print('Your grade: 2')

# elif(average>=55 and average<=69):
#     print('Your grade: 3')

# elif(average>70 and average<=84):
#     print('Your grade: 4')

# elif(average>85 and average<=100):
#     print('Your grade: 5')
# else:
#     print('There is an error in the inputs.')


#

import datetime

days = int(input ('On what date did your vehicle enter traffic?: '))

if days<=365:
    print('1. service interval')
    
elif days>365 and days<365*2:
    print ('2. service interval')
    
elif days> 365*2 and days<365*3:
    print('3. service interval')

else:
    print('wrong duration.')
    
    
    
    
  