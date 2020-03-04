'''
LEGB
Local, Enclosing, Global, Built-in
Python checks for scope in this order
'''
#Local is variables 
#Enclosing
#Global
#Built-in

#global Scope
x = 'global x'

def test():
    #if the local scope is given then the python chooses the local scope before choosing the global
    y = 'local y'
    x = 'local x'
    print(y)
    print(x)

test()
#print(y) # will fail because y is not set in the global scope. it only lives in the function
print(x) # will work because it is in the global

def test2():
    global x #tells the function to call the global statement. 
    print(x)
test2()

def test3(z):
    print(z)
test3('local z') #this become the local scope

#buit-in functions
#if you create a function that has the same name then your funcion will be overwritten. 

#enclosing scope
#checks if there is any thing in the inner function
#then checks if there is any local in the global function

a = 'global a'
def outer():
    a = 'outer a'

    def inner():
        a = 'inner a'
        print(a)

    inner()
    print(a)
outer()