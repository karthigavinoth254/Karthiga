name=input("Enter student name:")
marks=input("Enter marks:")
with open("marks.txt","a")as file:
    file.write(name+"-"+marks+"\n")
print("Data saved successfully")
with open("marks.txt","r")as file:
 for line in file:
    print(line.strip())
