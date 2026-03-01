'''try:
    file.open("interview prgrm.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
#manually create exception 
age=int(input("Enter age: ")
        if age<18:
            raise ValueError("Age must be 18 or above")
#custom error(create own error)
class invalidMarksError(Exception):
    pass:)
marks=int(input("Enter marks:"))
if marks<0 or marks>100:
    raise invalidMarksError("Marks should be 0 to 100")
print("Valid marks")'''
#ATM
try:
    balance = 5000
    amount = int(input("Enter withdraw amount: "))

    if amount > balance:
        raise Exception("Insufficient balance")
    else:
        print("Transaction successfully")
        print("Remaining balance:", balance - amount)

except ValueError:
    print("Enter a valid input")

except Exception as e:
    print(e)

finally:
    print("Thank you for using ATM")
#custom error or manual error
age=int(input("Enter age:"))
if age<18:
    raise ValueError("Age must be 18 or above")
else:
    print("Age is acceptable")
        






















    
    
