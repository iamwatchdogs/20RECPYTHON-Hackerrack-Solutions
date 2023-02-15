# Problem Statement: To sort the even elements in a list in descending order
#
# Sample Input 0: 7 5 6 9 8 3 4
# Sample Output 0: [8, 6, 4]
#
# Sample Input 1: 17 42 87 56 24 78 21
# Sample Output 1: [78, 56, 42, 24]
    
# My Solution:
print( sorted( [ i for i in list(map(int, input().split())) if i%2 == 0 ], reverse=True) )
