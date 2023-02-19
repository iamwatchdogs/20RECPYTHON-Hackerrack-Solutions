# Problem Statement: John had a list of each product sales count of a super market. By the end of the day he keeps
#                    track of the count of each product sales and elimanates the product sales count which are not 
#                    correctly recorded.
#
# Sample Input 0: 25 -8 63 -22 44 66 -5 77
# Sample Output 0: [25, 63, 44, 66, 77]

# My Solution:
print( [ i for i in list(map(int, input().split())) if i > 0 ] )
