num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is: ", sum)

variable1 = input("Enter the value of variable 1: ")
variable2 = input("Enter the value of variable 2: ")

print("Before swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)

variable1, variable2 = variable2, variable1

print("\nAfter swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("The perimeter of the rectangle is:", perimeter, "\nThe area of the rectangle is:", area)

