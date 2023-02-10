# Problem Statement: Function to find numbers which are divisible by 7 but are not a multiple of 5, between n1 and n2 (both included).
#
# Constraints: n1>0 n2>0
#
# Sample Input 0:
#         22
#         55
# Sample Output 0:
#         [28, 42, 49]
#
# Sample Input 1:
#         1
#         25
# Sample Output 1:
#         [7, 14, 21]

# My Solution: ( Maybe the Best Solution? )
print( [ i for i in range(int(input()),int(input())) if i%7 == 0 and i%5 != 0 ] )    
