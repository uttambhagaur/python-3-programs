#function in python 3
#def is used to define function

def prints():
    print("Welcome in Function Section")

#parameter function

def sumtwo(a,b):
    c=a+b
    print(c)

#parameter function with return

def multi(a,b):
    return a*b

#default argument

def fun(str,time=1):
    return str*time

prints()
sumtwo(5,6)
print(multi(6,8))
print(fun("one"))
print(fun("uttam",3))
