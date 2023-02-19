# Problem Statement: Addition of two matrices
#
# Sample Input 0:
#           2
#           3
#           1 2 3 4 5 6
#           4 5 6 7 8 9
# Sample Output 0:
#           5 7 9 
#           11 13 15
#
# Sample Input 1:
#           2
#           2
#           -11 2 3 4 
#           4 -5 6 7
# Sample Output 1:
#           -7 -3 
#           9 11 

# My Solution:
r = int(input())
c = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
for i in range(r):
    for j in range(c):
        print(l1.pop(0)+l2.pop(0),end=' ')
    print()
    
# My Friend's Solution:
r=int(input())
c=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[l1[i]+l2[i] for i in range(r*c)]
for i in range(r*c):
    if i%c==0 and i!=0:
        print()
    print(l3[i],end=" ")
