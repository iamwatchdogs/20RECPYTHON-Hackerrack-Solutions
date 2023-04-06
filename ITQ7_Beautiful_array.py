# Problem Statement:
#
#   Given an array of L integers and a number N, write a python function ‘beautifulCheck’ which takes ‘N’ and array of L integers as parameters 
#   to check whether the array is beautiful or not. An array is said to be beautiful if it satisfies the following conditions: 
#     1. All elements of array must lie between 1 and N (inclusive of 1 and N). 
#     2. Array must be unordered 
#     3. The array elements are unique. 
#   Print True if array is beautiful, False otherwise..
#
# Constraints:
#   0 < N < 10000.
#   0 < L < 10000.
#
# Sample Input 0:
#   5
#   4
#   1 2 3 4
# Sample Output 0:
#   False
# Explanation 0:
#   Array is in ascending order
#
# Sample Input 1:
#   8
#   5
#   4 7 2 5 6
# Sample Output 1:
#   True
# Explanation 1:
#   True, because array satisfies all the required conditions.

# My Solution:
def beautifulCheck(N, L):
    return all( i in range(1,N+1) for i in L ) and L != sorted(L) and L != sorted(L, reverse=True) and all( L.count(i) == 1 for i in L)
n = int(input())
l_len = int(input())
l = list(map(int, input().split()))
print(beautifulCheck(n,l))

# More readable Solution:
def beautifulCheck(N, L):
    check_range = all( i in range(1,N+1) for i in L )
    check_sorted = (L != sorted(L) and L != sorted(L, reverse=True))
    check_unique = all( L.count(i) == 1 for i in L)
    return check_range and check_sorted and check_unique

def __main__():
    n = int(input())
    l_len = int(input())
    l = list(map(int, input().split()))
    res = beautifulCheck(n,l)
    print(res)

__main__()

# My Friend's Solution:
def beautifulcheck(n1, n2):
    l= list(map(int, input().split()))
    if any(elem < 1 or elem > n1 for elem in l):
        return False
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    if len(set(l)) != len(l):
        return False
    return True
n1=int(input())
n2=int(input())
result = beautifulcheck(n1, n2)
print(result)
