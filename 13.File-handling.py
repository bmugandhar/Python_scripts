import os
os.getcwd()
os.chdir("C:\\Users\\rsairi\\data")
os.getcwd()

# File modes(r,r+,w,w+,a,a+,etc..)
# Open a file from mentioned path
ft=open('sample.txt','r')
print(ft.read())

ft=open('sample.txt')
print(ft.readline())
print(ft.readline())


ft=open('sample.txt')
print(ft.readline(),end='' )
print(ft.readline())

ft=open('sample.txt')
print(ft.readline(4))
print(ft.readlines())

# Write a file , It will create a new file
ft=open('sample1.txt','w') 
ft.write("line")

ft.write("bar")
ft.close()

ft=open('sample1.txt','w') 
ft.write("withcolor")
ft.close()

ft=open('sample1.txt','r')
print(ft.read()) 
ft=open('sample1.txt','a') 
ft.write("RED")
ft.close()

'''
ft=open('sample.txt','r')
ft1=open('test.txt','w') 

for f in ft:
    print(f)

for data in ft:
    ft1.write(data)
    
    
#close a file 
ft1.close()
'''
ft=open('sam1.jfif','r')
for f in ft:
    print(f)

ft=open('sam1.jfif','rb')
for f in ft:
    print(f)

ft=open('sam1.jfif','rb')
ft1=open('abc.jfif','wb')
for f in ft:
    ft1.write(f)

ft.close()
ft1.close()   
# to know whether file is closed or not. 
ft.closed
#To delete a file you must import os module and run its os.remove() function
import os
os.remove('mdata.txt')

#check the file exists
import os
if  os.path.exists('mdata.txt'):
    os.remove('mdata.txt')
else:
    print('The file does not exist')

#deleting a folder
import os
os.rmdir('x')    

'''########To list all the files and path in the folder###########'''
import glob

path = 'C:\\Users\\rsairi\\data'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)

###########################################
# Other file functions
ft=open('sample.txt','r+')
ft.tell()   # position of the control to read a file position
ft.read(5) 
ft.tell() 
ft.seek(0,1)   # to set the position
ft.tell()
ft.close()

#fp.seek(offset, from_what)
'''
where fp is the file pointer you're working with; offset means how many positions 
you will move; from_what defines your point of reference:

0: means your reference point is the beginning of the file
1: means your reference point is the current file position
2: means your reference point is the end of the file
if omitted, from_what defaults to 0.
'''
ft=open('sample.txt','r')
ft.seek(0,0)   # to set the position
next(ft)
ft.close()

# other file functions to know about file
ft.closed
ft.name
ft.mode
ft.fileno()

'''
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: "), fo.name

fid = fo.fileno()
print ("File Descriptor: "), fid

# Close opend file
fo.close()
'''

ft=open('date0808.txt','w+')
ft.read(3)
ft.truncate(3)
ft.close()


ft=open('test.txt','a+')
ft.write("end")
ft.read()
ft.read(10)
ft.close()
ft=open('test.txt','r+')
ft.readline()
ft.readlines()
ft.close()
ft=open('test.txt','r+')
print(ft.readline())
ft.flush

