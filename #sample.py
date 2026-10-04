#sample
#Arthimetic operations (+ - * / // % **)
print(5 + 3) #8
# / always returns float value
print(5/3) #1.666...
print(5//3) #1 (floor division)
print(5%3) #2 (modulo operation)
print(5**3) #125 (exponentiation)
print(5-3) #2 (subtraction)
print(5*3) #15 (multiplication)
# Exponentiation
print(5 ** 3) # → 125
print(72 ** 0.5) # → 8.485 (square root)
print(30 ** (1/3)) # → 3.107 (cube root)
#relational operators (==, !=, >, <, >=, <=)
print(5 == 3) #False
print(5 != 3) #True
print(5 > 3) #True
print(5 < 3) #False
print(5 >= 3) #True
print(5 <= 3) #False
print(5 == 5) #True
# Chained comparisons — unique to Python, reads like maths
x = 5
print(2 < x < 10) # → True (x is between 1 and 10)
print(0 <= x <= 5) # → True
print(5 < x < 10) # → False (x is not greater than 5)
#string comparisons  — lexicographic (letter by letter)
print("apple" < "banana") # → True (a comes before b)
print("apple" > "banana") # → False (a comes before b)
print("apple" == "banana") # → False (different words)
print("apple" != "banana") # → True (different words)
print("apple" < "Apple") # → False (lowercase a comes after uppercase A)
print("apple" > "Apple") # → True (lowercase a comes after uppercase A)
print("apple" == "Apple") # → False (different words)
print("apple" != "Apple") # → True (different words)
#comparison boolean with numbers
print(5 > 3) # → True
print(5 < 3) # → False
print(5 == 3) # → False
print(5 != 3) # → True
print(1 == True) # → True (True equals 1 in Python)
print(0 == False) # → True (False equals 0 in Python)
print(1 == False) # → False (1 does not equal 0)
#assignment operators (+=, -=, *=, /=, //=, %=, **=)
score = 0
score += 10 # score = score + 10
score -= 5 # score = score - 5
score *= 2 # score = score * 2
score /= 3 # score = score / 3
score //= 2 # score = score // 2
score %= 4 # score = score % 4
score **= 3 # score = score ** 3
print(score) # → 0.0 (final value of score after all operations)
# tuple assignment — assign different variables in one line
x, y, z = 1, 2, 3
print(x, y, z) # → 1 2 3
# multiple assignment — assign the same value to multiple variables
x = y = z = 0 # → all variables are assigned the same value
print(x, y, z) # → 0 0 0
# Swap variables — Pythonic way, no temporary variable needed
x, y = 1, 2
x, y = y, x
print(x, y) # → 2 1
# and — both conditions must be True
print((5 > 3) and (2 < 4)) # → True (both conditions are True)
# or — at least one condition must be True
print((5 > 3) or (2 > 4)) # → True (at least one condition is True)
# not — negates the boolean value
print(not (5 > 3)) # → False (5 is not greater than 3)
#bitwise operators (&, |, ^, ~, <<, >>)
# bin() shows the binary representation of any number
print(bin(5)) # → 0b101 (binary representation of 5)
print(bin(10)) # → 0b1010 (binary representation of 10)
# AND — 1 only where both bits are 1
print(5 & 3) # → 1 (binary: 101 & 011 = 001)
print(10 & 7) # → 2 (binary: 1010 & 0111 = 0010)
# OR — 1 where either bit is 1
print(5 | 3) # → 7 (binary: 101 | 011 = 111)
print(10 | 7) # → 15 (binary: 1010 | 0111 = 1111)
# XOR — 1 where bits are different
print(5 ^ 3) # → 6 (binary: 101 ^ 011 = 110)
print(10 ^ 7) # → 13 (binary: 1010 ^ 0111 = 1101)
# Left shift — multiply by powers of 2
print(5 << 1) # → 10 (binary: 101 << 1 = 1010)
print(5 << 2) # → 20 (binary: 101 << 2 = 10100)
# right shift — divide by powers of 2
print(5 >> 1) # → 2 (binary: 101 >> 1 = 10)
print(5 >> 2) # → 1 (binary: 101 >> 2 = 1)
# membership and identity operators (in, not in, is, is not)
# membership operators
print(3 in [1, 2, 3]) # → True (3 is in the list)
print(4 not in [1, 2, 3]) # → True (4 is not in the list)
# identity operators
print(3 is 3) # → True (same object)
print(3 is not 4) # → True (different objects)
# precedence in practice
# * before + (same as BODMAS)
print(5 + 3 * 2) # → 11 (3*2 is evaluated first)
print((5 + 3) * 2) # → 16 (parentheses change the order of operations)
# ** is right to left
print(2 ** 3 ** 2) # → 512 (3**2 is evaluated first, then 2**9)
print((2 ** 3) ** 2) # → 64 (parentheses change the order of operations)
# Comparison before logical operators
print(5 > 3 and 2 < 4) # → True (comparison evaluated first)
print(5 > 3 or 2 > 4) # → True (comparison evaluated first)
# When unsure — always use parentheses for clarity
print((5 > 3) and (2 < 4)) # → True (explicitly shows the order of operations)
print((5 > 3) or (2 > 4)) # → True (explicitly shows the order of operations)