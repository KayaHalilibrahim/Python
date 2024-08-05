
# Calculating circle area and circumference
# r = radius


pi = 3.14
r = input ('radius: ')

r = float(r) # because r is string
area = pi * (r**2)
circumference=2*pi*r

print ('Area of circular: ',area)
print ('Circimference of circular: ', circumference)   

print('\nCircumference of circular: ', round(circumference, 2))  # more clearly

print()
print ('Arear: ',area, ' Circumference: ', round(circumference))