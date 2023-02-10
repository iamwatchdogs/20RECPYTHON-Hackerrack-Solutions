# Problem Statement: write a program to insert element at a given position in a list (lists)
#
# Sample Input 0:
#          10 20 30 40 50
#          80
#          3
# Sample Output 0:
#          [10, 20, 30, 80, 40, 50]

# My Solution:
l = list(map(int,input().split()))
n = int(input())
p = int(input())
l = l[:p] + [n] + l[p:]
print(l)

# Best Solution:
l = list(map(int, input().split()))
n = int(input())
p = int(input())
l.insert(p, n)
print(l)
