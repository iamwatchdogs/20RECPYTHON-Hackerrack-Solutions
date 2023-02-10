# Problem Statement: Program to find sum of all the elements in a list (Lists)
#
# Sample Input 0: 3 7 8
# Sample Output 0: 18

# My Solution:
from functools import reduce
print( reduce(lambda a,b:a+b,list(map(int,input().split()))) )

# Note that to use reduce we have to import it from the 'functools' package/module.
# Syntax of reduce() method: reduce(function, iterable[, initializer])
#
# For example,
#   Say you want to find the product of all the elements in a list and you want to
# write an one-liner code for it. then you use an lambda function to create a
# binary function ( which takes 2 arguments as i/p ) to find the product.
#
#                           lambda x,y: x*y
#
# Then you use reduce() method, where you pass the lambda function as your 1st argument
# and the input list as the second argument.
#
#                      reduce( lambda x,y: x*y, input_list )
#
# Now, the reduce() method will calculate the total product of the elements present in the
# list. This is done by taking 2 elements first and computing the answer and passing it in
# the place of 'x' and for 'y' it will go for next element in the list.
