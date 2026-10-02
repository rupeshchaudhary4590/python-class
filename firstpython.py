# this is the single line comment ctrl + /
""" This is a multi-line comment """
name = "rupesh"
age = 21
address = "birgunj"
print( "my name is" +name + "my age is" +str(age) +"address is" +address)
print(f"my name is {name}, age is {age}, and address is {address}")

print("my name is %s, age is %d, and my address is %s" %(name,age,address))

print("my name is {0}, age is {1}, and my address is {2}".format(name,age,address))