message = ' Hello dear. My name is Halil Kaya.'

message=message.upper() # writes all characters in capital letters.
message=message.lower()#writes all characters in lower case.
message = message.title() # capitalizes the first letter of each word.
message = message.capitalize()  # capitalizes the first letter of first word.

print (message)

parola = '  12334'

password = parola.strip() # removes leading spaces.
print (password)

message = message.split() # separates the next word with each space character.

print (message)
print (message[3][1]) # name -> a

message = ' '.join(message)  #It is used to combine words that we cannot separate.  message = '---'.join(message)
print (message)  


print (message.find('my'))  # it give index of first letter of word.

isFound = message.startswith('H')
print (isFound)

 
isFound = message.endswith('.')
print (isFound)

message = message.replace('halil','ibrahim') # change word.
print (message)


message = message.center(50)  # hello dear. my name is ibrahim kaya. -> 36 + 7 characters left and right leave space.
print (len(message))