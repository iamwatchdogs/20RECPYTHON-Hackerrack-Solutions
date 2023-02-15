# Problem Statement:
#   display the last n elements in a list(lists)
#   if n value is greater than length of list then display message "input must be with in range of length"
#
# Constraints: input must be with in the range of length of list
#
# Sample Input 0:
#       3 4 5 2 6 8 9
#       4
# Sample Output 0:
#       [2, 6, 8, 9]
#
# Sample Input 1:
#       56 78 21 34 23 97 85 21
#       5
# Sample Output 1:
#       [34, 23, 97, 85, 21]

l = list(map(int, input().split()))
n = int(input())
print( l[len(l)-n:] if n < len(l) else 'input must be with in range of length' )
