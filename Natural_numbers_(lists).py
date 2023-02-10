# Problem Statement: Write a program to display sum of natural numbers for a individual list of elements (lists)
#
# Constraints: List elements should be positive
#
# Sample Input 0: 2 5 3 1
# Sample Output 0: 25
    
# My Solution:
from functools import reduce
print( reduce(lambda a,b:a+b, map(lambda n:n*(n+1)//2, list(map(int,input().split()))) ) )
#      ---------------------  --------------------------------------------------------
#       Sum up whole list           update the values of each element with 
#                                   sum_of_natural_numbers() formulated value
