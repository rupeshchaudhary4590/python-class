#assigning variables.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your location: ")

#concate method
print("my name is " + name + ", age is " + str(age) + ", and address is " + address) # this is the concantation of string and interger using + operator.
print(f"my name is {name}, age is {age}, and address is {address}") # this is the f-string method to print the string and integer.
print("my name is %s, age is %d, and my address is %s" %(name,age,address)) # this is the old method to print the string and integer using % operator.
print("my name is {0}, age is {1}, and my address is {2}".format(name,age,address)) # this is the new method to print the string and integer using format() method.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

sum1 = num1 + num2
print(f"The sum of {sum1} and type is {type(sum1)}")

sum2 = num3 + num4
print(f"The sum of {sum2} and type is {type(sum2)}")