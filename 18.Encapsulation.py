#Protected members
#Private members
'''
Protected members (in C++ and JAVA) are those members of the class which cannot be 
accessed outside the class but can be accessed from within the class 
and it’s subclasses. 
In python by prefixing the name of the member by a single underscore “_”.
'''


# Python program to 
# demonstrate protected members 
  
  
# Creating a base class 
class Base: 
    def __init__(self): 
          
        # Protected member 
        self._a = 2
  
# Creating a derived class     
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling protected member of base class: ") 
        print(self._a) 
  
obj1 = Derived() 
          
obj2 = Base() 
  
# Calling protected member 
# Outside class will  result in  
# AttributeError 
print(obj2.a) 
########################################################
'''
Private members are similar to protected members, the difference is that the class members
declared private should neither be accessed outside the class nor by any base class. 
However, to define a private member prefix the member name with double underscore “__”.
'''
# Python program to  
# demonstrate private members 
  
# Creating a Base class 
class Base: 
    def __init__(self): 
        self.a = "Optum"
        self.__c = "Optum"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling private member of base class: ") 
        print(self.__a) 
# Driver code 
obj1 = Base() 
print(obj1.a) 
  
# Uncommenting print(obj1.c) will 
# raise an AttributeError 
  
# Uncommenting obj2 = Derived() will 
# also raise an AtrributeError as 
# private member of base class  
# is called inside derived class 
#########################################################

