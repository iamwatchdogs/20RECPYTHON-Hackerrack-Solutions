# Problem Statement: Kavisha has a set of items where she wants to find the cube of items within a specified range
#
# Constraints:
#   List should not be empty
#   Range < length of the List
#
# Sample Input 0:
#       3 2 4 7 9 5 8
#       3
# Sample Output 0:
#       [27, 8, 64, 7, 9, 5, 8]
#
# Sample Input 1:
#       5 2 3 4
#       6
# Sample Output 1:
#       Invalid Range

# My Original Solution:
l = list(map(int,input().split()))
n = int(input())
print( 'Invalid Range' if n >= len(l) else [ l[i]**3 for i in range(n) ]+l[n:] )

# My Solution ( More Readable ):
l = list(map(int, input().split()))
n = int(input())
if n >= len(l):
    print("Invalid Range")
else:
    l = [x**3 for x in l[:n]] + l[n:]
    print(l)
