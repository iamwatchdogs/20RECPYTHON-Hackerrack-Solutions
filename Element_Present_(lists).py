# Problem Statement: Every day teacher will check whether the student with in the class or out side of the class. 
#                    if he is present in the class print 'YES' otherwise print 'NO'(lists)
#    
# Sample Input 0:
#         10 20 30 40 50
#         20
# Sample Output 0:
#         YES
#
# Sample Input 1:
#         30 60 78 21 89
#         56
# Sample Output 1:
#         NO

# My Solution:
l = list(map(int,input().split()))
n = int(input())
print( 'YES' if n in l else 'NO')
