# Problem Statement: Maximum element of principal diagonal in a matrix (Lists)
#
# Sample Input 0:
#                   3                       // Row
#                   3                       // Colns
#                   11 2 33 4 56 6 77 8 9   // matrix
# Sample Output 0:
#                   56
# Sample Input 1:
#                   2
#                   3
#                   11 22 33 4 12 33
# Sample Output 1:
#                   Row and Column size should be same

# My Solution:
r,c = int(input()),int(input())
l = list(map(int,input().split()))
print( 'Row and Column size should be same' if r!=c else max([ l[i] for i in range(r*c) if i%(r+1) == 0 ]) )

# My Friend's Solution ( More readable ):
r,c = int(input()),int(input())
l = list(map(int,input().split()))
if r!=c:
    print("Row and Column size should be same")
else:
    t=[]
    for i in range(r*c):
        if i%(r+1)==0:
            t.append(l[i])
    print(max(t))
