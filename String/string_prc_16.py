import string

str = "Hello"
str1="23"
str2="Hello0319"

#isalpha(), isdigit(), isalnum()
print(f"Result of isalpha() is : {str.isalpha()}")
print(f"Result of isdigit() is : {str1.isdigit()}")
print(f"Result of isalnum() is : {str2.isalnum()}")

str3 = "Hello, This is Python Programming !"

#upper() and lower()
a = str3.upper()
b = str3.lower()
print(f"\nUppercase : {a}")
print(f"Lowercase : {b}")

#isspace() and whitespace
str = "hello python"
print("String contains only space : ",str)
x = str.isspace()
print("String contains only space : ",x)
str = "\n \t"
y = all(ch in string.whitespace for ch in str)
print("String contains only whitespace : ",y, "\n")