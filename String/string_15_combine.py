#Combination of upper(), lower() & isspace() and whitespace
import string
str3 = "Hello, This is Python Programming !"

#upper() and lower()
a = str3.upper()
b = str3.lower()
print(f"\nUppercase : {a}")
print(f"Lowercase : {b}")
print("\n")

#isspace() and whitespace
str = "hello python"
print("String : ",str)
x = str.isspace()
print("String contains only space : ",x)
str = "\n \t"
y = all(ch in string.whitespace for ch in str)
print("String contains only whitespace : ",y, "\n")