'''#dictionary comprehension
#square 
nums=[1,2,3,4,5]
square_dict={x:x*x for x in nums}
print(square_dict)'''
#print odd and even in dictionary
nums=[1,2,3,4,5]
square_dict={x:"even" if x%2==0 else "odd" for x in nums}
print(square_dict)
#dictionary
#create dictionary
student={"name":"vinoth","age":32,"marks":100,"year":2019,"work":"data analyst"}
print(student)
print(student["year"])
#update
print(student.get("age"))
student["age"]=33
print(student)
student.update({'gender':'male'})
print(student)
student.update({'year':2020})
print(student)
#pop()
print(student.pop("work"))#---print what the value in pop
student.popitem()#----remove last value
print(student)
#del
del student["marks"]
print(student)
#clear
student.clear()
print(student)
#---------------------------------------------------
student={"name":"vinoth","age":32,"marks":100,"year":2019,"work":"data analyst"}
for i in student:
    print(i)#-----print keys
for i in student:
    print(student[i])#-----------print values
print(student.keys())#---keys as list
print(student.values())#---keys as values
for i in student.items():
    print(i)
for i,j in student.items():
    print(f"keys={i} value={j}")
#default()
    student={"name":"vinoth","age":32,"marks":100,"year":2019,"work":"data analyst"}
    print(student.setdefault("Category","topper"))
#dictionary comprehension
    nums=[1,2,3]
    square_dict={x:x*x for x in nums}
    print(square_dict)
#dictionary comprehension odd or even
    nums=[1,2,3]
    square_dict={"even"if x%2==0 else "odd" for x in nums}'''
