import random


rnumber = random.randint(1,100)

#count = int(input('How many times do you want to try: '))
count=5

point = 100 /count



while count>0:
    count-=1
    number=int(input('Please enter a number between 1 and 100: '))
    if count==0:
        print('Your trial period has expired.')
        break
    if(number==rnumber):
       print(f'Congratulations you found it: {rnumber}')
       break
    elif(number>rnumber):
       print('down')
    elif(number<rnumber):
       print('Up')
    else:
       print("You couldn't find it")
   

result = (count+1)*point

print ('Your Point:',result)
print('random number:',rnumber)



