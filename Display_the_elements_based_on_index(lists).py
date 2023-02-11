# Problem Statement: To display the elements in the list starting from nth index
#
# Sample Input 0:
#       10 20 30 40 50
#       2
# Sample Output 0:
#       [30, 40, 50]
#
# Sample Input 1:
#       5 77 12 8 99
#       5
# Sample Output 1:
#       elements not found

# My Solution:
l = list(map(int, input().split()))
n = int(input())
print( l[n:] if len(l) > n else 'elements not found' )
