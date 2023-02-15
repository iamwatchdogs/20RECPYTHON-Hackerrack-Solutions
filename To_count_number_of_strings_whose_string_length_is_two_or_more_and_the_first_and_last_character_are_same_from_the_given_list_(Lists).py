# Problem Statement: To count number of strings whose string length is two or more and the first and
#                    last character are same from the given list (Lists)
#
# Constraints: String length >= 2
#
# Sample Input 0: abc aba abb ccc
# Sample Output 0: 2

# My Solution:
print( len( [ i for i in input().split() if i.endswith(i[0]) ] ) )

# Alternative Solution:
print( len( [ i for i in input().split() if i[0] == i[len(i)-1] ] ) )
