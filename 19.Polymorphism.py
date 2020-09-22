##################################Duck Typing#############################
'''Poly -> Many
Morphism-> forms
we behave in different ways when we are in different places...eg..like off and house
Object will have multiple forms
There are 4 ways of implementing polymorphism
Duck typing
Operating overloading
Method overloading
Method overriding
'''
class Spyder:
    def execute(self):
        print("Compliling")
        print("Running")

       
class laptop:
     def code(self,ide):
        ide.execute()
        
ide=Spyder()

lap1=laptop()
lap1.code(ide)

#####################################
class Spyder:
    def execute(self):
        print("Compliling")
        print("Running")

class Myeditor:
     def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compliling")
        print("Running")

###########JAVE we have interface############
#if there is an object ide and it has a method execute we are not concerned which class it is
        #this is duck typing
class laptop:
     def code(self,ide):
        ide.execute()
        
ide=Myeditor()

lap1=laptop()
lap1.code(ide)


####################################

