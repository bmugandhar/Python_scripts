'''###################Exception Handling###################'''

a=5
b=2

print(a/b)

###################User will not understand what the error is#####################################
a=5
b=0

print(a/b)

print("end")
#########################apply try block###############################
a=5
b=0

try:
    print(a/b)

except Exception:
     print("U cannot divide the number by zero")

print("end")
##################################################################
a=5
b=2

try:
    print(a/b)

except Exception:
     print("U cannot divide the number by zero")

print("end")
########################### e is objet of exception #####################################
a=5
b=2

try:
    print(a/b)

except Exception as e:
     print("U cannot divide the number by zero", e)

print("end")
#############################################################333
a=5
b=2

try:
    print("Resource open")
    print(a/b)
    print("Resource closed")
except Exception as e:
     print("U cannot diveide the number by zero", e)

print("end")
################################################################
a=5
b=0

try:
    print("Resource open")
    print(a/b)
    print("Resource closed")
except Exception as e:
     print("U cannot divide the number by zero", e)

print("end")
#############################################################
#finally block will be executed if we get error as well as if we don't get the error
a=5
b=0

try:
    print("Resource open")
    print(a/b)
    
except Exception as e:
     print("U cannot diveide the number by zero", e)

finally:
    print("Resource closed")
#########################################################
a=5
b=2

try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter the number"))
    print(k)
except Exception as e:
     print("U cannot diveide the number by zero", e)

finally:
    print("Resource closed")
##########################################################
a=5
b=0


    
try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter the number"))
    print(k)
   
except ZeroDivisionError as e:
     print("U cannot diveide the number by zero", e)

except ValueError as e:
     print("Invalid Input")

except Exception as e:
     print("Something wrong")
     
finally:
    print("Resource closed")

####################################################################    
ft=open('date1209.txt')
print(ft)

locals()['__builtins__']

try:   
    a = 10/0  
    print (a)
except ArithmeticError:   
        print("This statement is raising an arithmetic exception.")
else:   
    print ("Success.")
    

try:   
    a = 10/2  
    print (a)
except ArithmeticError:   
        print("This statement is raising an arithmetic exception.")
else:   
    print ("Success.")
#####################################################################3
try:  
    a = [1, 2, 3]  
    print (a[5])
except LookupError:  
    print ("Index out of bound error.")
else:  
    print ("Success")

try:  
    a = [1, 2, 3]  
    print (a[1])
except LookupError:  
    print ("Index out of bound error.")
else:  
    print ("Success")

#####################################################################

