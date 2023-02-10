# Problem Statement: Check whether the maximum element in the list is even or odd(lists)
#
# Sample Input 0: 11 56 78 21 43
# Sample Output 0: even

# My Solution:
print( 'even' if max(list(map(int,input().split())))%2 == 0 else 'odd' )
