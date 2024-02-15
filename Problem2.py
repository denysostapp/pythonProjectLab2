import math

radius = float(input("Enter the radius of the circle:"))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print("The area of circle:", area, "Circumference:", circumference)

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("The temperature in Fahrenheit is:", fahrenheit)
print("The temperature in Celsius:", celsius)


def solve_quadratic(a, b, c):
    """Function to solve a quadratic equation"""
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Given coefficients
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

# Solving the quadratic equation
root1, root2 = solve_quadratic(a, b, c)

# Displaying the results
print("The roots of the quadratic equation:")
print("Root 1:", root1)
print("Root 2:", root2)

principal = 5000  # dollars
apr = 3  # Annual percent interest rate
years = 10

# Convert APR to decimal
rate_decimal = apr / 100

# Calculate compound interest
investment_value = principal * (1 + rate_decimal)**years
interest_earned = investment_value - principal

# Display the result
print("The investment value after", years, "years is $", round(investment_value, 2))
print("The interest earned is $", round(interest_earned, 2))

