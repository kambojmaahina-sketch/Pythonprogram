'''functions--set of instructions under name
part of program also known as sub program
always ready to perform task we need to call it
during call if it expect some arguments (dat which we pass to function) then we need to 
pass those arguments to function

#syntax-- 
def function-name(arg1,arg2,...)
...
...
return[value]

#types-some function accept data some return
Accept    return
   Y         Y   
   N         Y   
   Y         N   
   N         N   

#Need-- 
when we are unable to perform a job
perform a task again and again after sometime
'''
def msg():
    "This is msg function does not accept argument and return also"
    print("Hello Welcome to function.")
    print("I am msg function does not accept and return")

def total(n1,n2):
    "sum of 2 nos"
    print(f"The sum is {n1+n2}")

def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def table(num):
    for i in range(1,num+1):
        print(f"{num}x{i}={num*i}")

def sayhello(name="Guest"):
    print(f"Hello {name} Welcome to function")

def getpi():
    return 3.14


__name__="MyFun"

'''The .py file in python also known as module. 
--can be imported in the project into another .py file
Its function can be accessible in that .py file which is importing it'''