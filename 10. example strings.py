
website= 'https://www.kayahalil.com'
course ='I am learning python from beginner to advanced level.'

lengthCourse = len(course)
print(lengthCourse)

print (website[8:11]) # www

print (website[-3:len(website)])   # com
print ('firs 15 character: ' + course[:15] + ' - last 15 character: ' + course[-15:])



result = course[::-1]  # Writes in reverse
print (result)

s ='12345' * 5  # Prints 12345 5 times.
print (s[::5])  #only write ones.


name, surname, age, job ='Bora', 'Yılmaz', 32, 'Engineer'

print (f'My name is {name} {surname}, I am {age} years old and I am a {job}')

message ='Hello world'
message = message[:6] + 'W' + message[7:len(message)] 

print (message)


s = 'abc ' *3
print (s)
