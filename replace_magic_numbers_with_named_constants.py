FORCE_CONST = 8.9875517923
X_VALUE = 1e9
# First Section
# Given two point charges, calcualte the electric force exerted on them.
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force = FORCE_CONST*X_VALUE * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
TWO = 2
ZERO = 0
num = int(input('Enter an integer number: '))
if num % TWO == ZERO:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")