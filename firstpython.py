# this is the single line comment ctrl + /
""" This is a multi-line comment shift +alt +a """
# assigning variables.
name = "rupesh"
age = 21
address = "birgunj"
print( "my name is" +name + "my age is" +str(age) +"address is" +address) # this is the concatenation of string and interger using + operator.
print(f"my name is {name}, age is {age}, and address is {address}") # this is the f-string method to print the string and integer.

print("my name is %s, age is %d, and my address is %s" %(name,age,address)) # this is the old method to print the string and integer using % operator.

print("my name is {0}, age is {1}, and my address is {2}".format(name,age,address)) # this is the new method to print the string and integer using format() method.