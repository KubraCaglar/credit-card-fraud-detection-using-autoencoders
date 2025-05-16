
# ***************************************
#              UTILITIES
# ***************************************

# This function calculates the factorial of a number using recursion which is a method where the function calls itself.
# Factorial is used in combinatorics, algebra, and mathematical analysis.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# ***************************************
#              END
# ***************************************
