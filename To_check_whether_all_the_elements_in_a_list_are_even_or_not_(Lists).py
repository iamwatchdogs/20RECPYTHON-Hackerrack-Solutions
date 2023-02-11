# Problem Statement:
#     To check whether all the elements in a list are even or not (Lists):
#     Display True if all the elements in list are even
#     Display False even if one element in the list is odd

# Sample Input 0: 2 4 8 
# Sample Output 0: True

# My Solution:
print( all(i%2 == 0 for i in list(map(int, input().split()))) )
