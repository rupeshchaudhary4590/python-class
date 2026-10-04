#membership and identity

a = [1, 2, 3]
b = [1, 2, 3]

c = a
print(a is b)  # False, because a and b are different objects in memory value compares
print(a == b) # True, because a and b have the same content
print(a is c)  # True, because a and c refer to the same object in memory
print(id(a)) # Prints the memory address of the object a
print(id(b)) # Prints the memory address of the object b
print(id(c)) # Prints the memory address of the object c
