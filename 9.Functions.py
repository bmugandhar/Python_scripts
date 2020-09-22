#*** Loop function in print

#x={1:'raju',2:'hyd',3:'first'}
#print([i for i in x.items()])
#print([i for i in x.keys()])


# function definationn and calling
def disp():
    print ('python program')
disp()    

#Function with arguments
def stddt(name,rank):
    print('student Name: ' , name,'student Rank: ', rank )
stddt('ram',2)

# function with default arguments

def add(a,c,b=40):
    tot = a+b+c
    print ('sum is:  ' , tot)

add(10,20,5)
add(10,20)

# Function with nothing return 
def pnt():
    print('hello first function')
    return 
pnt()

# function with return value
def add(a,b,c):
    tot = a+b+c
    return tot

total = add(10,5,20)
print(total)


# input as variable number of arguments for function
def dis(*argv):
    for i in argv:
        print (i)
#    return

dis('math','eng','social')


def dis(name,*argv):
    print('student details: ', name)
    for i in argv:
        print (i)
#    return

math=input('enter math marks:')
eng=input('enter math eng:')
social=input('enter math social:')

dis('Ram',math,eng,social)

# input as keyword arguments for function

def kwargsfun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
kwargsfun(stname ='Abhi',stclass= 2, rank=3,school='dps')


def kwargsfun(a,**kwargs):  
    print('roll number: ' , a)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
kwargsfun(10,stname ='Abhi',stclass= 2, rank=3,school='dps')


# Global and local variables 
sum = 0
def add(a,c,b):
    sum = a+b+c
    print ('in function sum : ' , sum )
    return sum
print ('before function call sum is : ' , sum )
add(10,20,5)
print ('after function call sum : ' , sum )


# Fibonacci numbers module
print ("Module program calling")
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

fib(50)

# return Fibonacci series up to n write in list
def fib2(n):  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib2(100)
#dir(functions)
locals()
globals()

#lambda keyword is used to create anonymous functions
'''Lambda functions can have any number of arguments but only one expression. 
The expression is evaluated and returned. 
Lambda functions can be used wherever function objects are required.'''
#syntax
lambda arguments: expression

double = lambda x: x * 2
double = lambda x: x*x*x

# Output: 10
print(double(5))

# by using def above and below are same
def double(x):
   return x * 2

print(double(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Lambda functions are used along with built-in functions like filter(), map()
'''The function is called with all the items in the list and a 
new list is returned which contains items for which the function evaluats to True.'''
# Program to filter out only the even items from a list
#The % is called the modulo operator. Of course when the remainder is 0, the number is even.

def is_even(n):
    return n%2==0
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(is_even, my_list))
print(new_list)
###################################################
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))
#new_list = lambda my_list: (my_list%2 == 0) 

# Output: [4, 6, 8, 12]
print(new_list)

'''The function is called with all the items in the list and a new list is 
returned which contains items returned by that function for each item'''
# Program to double each item in a list using map()

def updte(n):
    return n+2
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(updte, my_list))
print(new_list)
###############################################
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
##################################################
from functools import reduce
#reduce(function, sequence)
def add_all(a,b):
    return a+b
sum=reduce(add_all,new_list)
print(sum)
##################################################

sum=reduce(lambda a,b: a+b, new_list)
print(sum)
#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

##############################################################

#id() is an inbuilt function in Python.
#This is random but when running in the same program, it generates unique and same identity. 
id(object)

id(1025)

id("geek")

str1 = "geek"
print(id(str1)) 
  
str2 = "geek"
print(id(str2)) 
  
# This will return True 
print(id(str1) == id(str2)) 
  
# Use in Lists 
list1 = ["aakash", "priya", "abdul"] 
print(id(list1[0])) 
print(id(list1[2])) 
  
# This returns false 
print(id(list1[0])==id(list1[2])) 

####################Global vs. Local variables##############################################
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;

# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 
