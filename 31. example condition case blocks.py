
#Check if the entered number is between 0 and 100.

# number = int (input ('Enter a number: '))
# if number>=0 and number<=100:
#     print ('this number is between 0 and 100')
    
# else:
#     print ('this number is not between 0 and 100')



#2 Check if the entered number is positive and even.
number = int (input ('Enter a number: '))

if number>0:
    if number%2==0:
        print('this number is positive and even.')
    else:
        print('this number is not even.')
else:
    print ('This number is positive (negative or 0.)')


