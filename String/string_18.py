import string

#isspace() and whitespace
str = "hello python"
print("String contains only space : ",str)
x = str.isspace()
print("String contains only space : ",x)
str = "\n \t"
y = all(ch in string.whitespace for ch in str)
print("String contains only whitespace : ",y, "\n")