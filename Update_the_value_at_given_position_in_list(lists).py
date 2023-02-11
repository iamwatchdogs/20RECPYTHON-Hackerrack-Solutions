# Problem Statement:
#     To update the value at given position in list and display updated list
#     if given position exceeds the length of list then display "element not found for updation"
#
# Sample Input 0:
#           10 2 25 7 86
#           20
#           3
# Sample Output 0:
#           [10, 2, 25, 20, 86]
#
# Sample Input 1:
#           22 77 6 88 9
#           56
#           5
# Sample Output 1:
#           element not found for updation

# My Solution:
l = list(map(int, input().split()))
n = int(input())
p = int(input())
if p < len(l):
    l[p] = n
    print(l)
else:
    print('element not found for updation')
    
# Alternative Solution:
l = list(map(int, input().split()))
n = int(input())
p = int(input())
try:
    l[p] = n
    print(l)
except:
    print('element not found for updation')
