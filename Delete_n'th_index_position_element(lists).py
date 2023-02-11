# Problem Statement: To delete nth index position element in a list(lists) If element not found display the message as 'element not found for deletion'
#    
# Sample Input 0:
#         10 20 30 40 50 
#         2
# Sample Output 0:
#         [10, 20, 40, 50]
#
# Sample Input 1:
#         56 23 87 96 21 92
#         4
# Sample Output 1:
#         [56, 23, 87, 96, 92]

# My Solution:
l = list(map(int, input().split()))
n = int(input())
try:
    l.pop(n)
    print(l)
except:
    print( 'element not found for deletion' )
    
# Best Solution:
l = list(map(int, input().split()))
n = int(input())
if n >= len(l):
    print("element not found for deletion")
else:
    l.pop(n)
    print(l)
