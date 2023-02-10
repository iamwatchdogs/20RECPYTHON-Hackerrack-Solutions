# Problem Statement: Check whether a number is in a given range(functions)
#
# Sample Input 0:
#          2 10
#          4
# Sample Output 0:
#          4 is in the range
#
# Sample Input 1:
#          2 10
#          12
# Sample Output 1:
#          The number is outside the given range.

# My Solution: ( Maybe the Best Solution? )
l=list(map(int,input().split()))
n=int(input())
print( f'{n} is in the range' if n in range(l[0],l[1]+1) else 'The number is outside the given range.')
