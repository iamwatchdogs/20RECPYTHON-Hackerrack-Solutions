# Problem Statement: Reverse a given matrix elements
#
# Sample Input 0:
#                   3                           // Row
#                   3                           // Cols
#                   123 12 13 4 56 6 73 81 19   // matrix
# Sample Output 0:
#                   [[321, 21, 31], [4, 65, 6], [37, 18, 91]]

# Sample Input 1:
#                   2
#                   3
#                   1234 34 4 37 989 901
# Sample Output 1:
#                   [[4321, 43, 4], [73, 989, 109]]

# My Solution:
r = int(input())
c = int(input())
res = [int(i[::-1]) for i in input().split()]
print([ [ res.pop(0) for i in range(c) ] for i in range(r)])

# My Friend's Solution ( More Readable ):
r=int(input())
c=int(input())
l=input().split()
res=[int(i[::-1]) for i in l]
out=[]
k=0
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(res[k])
        k+=1
    out.append(temp)
print(out)
