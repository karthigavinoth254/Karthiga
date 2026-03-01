#Search methods
print("hello".isalpha())
print("123".isdigit())
print("hello123".isalnum())
print("hello".isupper())
print("hello".islower())
print("hello".startswith("he"))
print("hello".endswith("lo"))


#Regular Expression
#search
import re
txt="The rain in spain"
x=re.search("The spain",txt)
if x:
    print("Match found")
else:
    print("Match not found")
#serach()
import re
txt="The rain in spain"
x=re.search("The rain",txt)
if x:
    print("Match found")
else:
    print("Match not found")
#findall()
import re
txt="The rain in spain"
x=re.findall("ai",txt)
print(x)
#split()
import re
txt="The rain in spain"
x=re.split("\s",txt)
print(x)
import re
txt="The rain in spain"
x=re.split("a",txt)
print(x)
#sub
import re
txt="The rain in spain"
x=re.sub("\s","9",txt)
print(x)
import re
txt="The rain in spain"
x=re.sub("\s","#",txt,2)
print(x)
import re
txt="The rain in spain"
x=re.findall(".*ai",txt)
print(x)
import re
txt="The rain in spain"
x=re.subn("ai","-",txt,2)
print(x)
import re
txt="The rain in spain"
print(re.findall("\w+","My number is 123"))'''
#email id
import re
email="karthigavinoth254@gmail.com"
pattern=r^[\w\.t]+@[\w.\.-]+\.\w+$
if re.search(pattern,email):
    print("Valid email")
'''
