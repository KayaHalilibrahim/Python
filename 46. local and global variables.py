
#global scope
x = 'global x'

def function():
    #local scope
    #x = 'local x'
    print (x)
    
    
function()
print(x)



#-----------------------------
print()

name = 'çınar'

def changeName(new_name):
    name = new_name
    print(name)
    
    

changeName('Ada')
print(name)



#-----------------------------
print()




name = 'Global string'

def greeting ():
    #name = 'Çınar'
    
    def hello ():
        # name = 'Ahmet'
        print('Hello ' + name)
    
    
    hello()

greeting()
print(name)


#-----------------------------
print()


x = 50

def test(x):
    print (f'x: {x}' )
    
    x = 100
    print(f'Changed x to {x}')
    
    
    
test(x)
print(x)



#-----------------------------
print()


y = 60

def test():
    global y
    print (f'y: {y}' )
    
    y = 200
    print(f'Changed y to {y}')
    
    
    
test()
print(y)