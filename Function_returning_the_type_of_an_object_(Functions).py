# Problem Statement: Function to return the type of an input
#
# Constraints: Input only python defined objects
#
# Sample Input 0: 10
# Sample Output 0: int
#
# Sample Input 1: 'uma shankar'
# Sample Output 1: str
#
# Sample Input 2: [1,2,3,4]
# Sample Output 2: list
#
# Sample Input 3: ()
# Sample Output 3: tuple

# My Solution: ( Maybe the best solution? )
print(type(eval(input())).__name__)

# Note:
# The eval() function evaluates the input string as a valid python expression and returns the result.
# The type() function takes an object as an argument and returns its type.
# The .__name__ attribute is used to retrieve the name of the type returned by the type() function and print it.
