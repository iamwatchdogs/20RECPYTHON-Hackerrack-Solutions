# Problem Statement: krishna having one list and umashankar having some other list. 
#                    Now combining these two lists into a single list(list)
#
# Sample Input 0:
#           10 20 30 40 50
#           60 70 80 90
# Sample Output 0:
#           [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# Sample Input 1:
#           1 4 2 8 9
#           2 3 4
# Sample Output 1:
#           [1, 4, 2, 8, 9, 2, 3, 4]

# My Solution:
print( list(map(int, input().split())) + list(map(int, input().split())) )
