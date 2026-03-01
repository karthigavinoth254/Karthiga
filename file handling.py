#file open and read methods
file=open("interview prgrm.txt",'r')
print(file.read())
file.close()
file=open("interview prgrm.txt",'r')
print(file.read(5))#(5)character
file.close()
file=open("interview prgrm.txt",'r')
file.close()
#file write
file=open(r'C:\Users\Admin\OneDrive\Desktop\Python\file handling.py')
print(file.write("This is interview programs"))
file.close()
#file.append
file=open(r'C:\Users\Admin\OneDrive\Desktop\Python\file handling.py')
print(file.append("This text file shows"))
file.close()
