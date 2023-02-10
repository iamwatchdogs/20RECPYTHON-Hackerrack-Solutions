# Problem Statement: Peter has a list containing items and he wants to find out the unique items
#
# Constraints: list of items > 1
#
# Sample Input 0: 1 3 2 1 1 3 3 2 2 4 5
# Sample Output 0: [1, 3, 2, 4, 5]

# My Solution:
res=[]
for i in map(int,input().split()):
    if i not in res:
        res.append(i)
print(res)

# Best Solution:
res = set()
for i in map(int, input().split()):
    res.add(i)
print(list(res))

# Note that the best solution is the actual solution to the problem statement
# but in hackerrack, this code might give the expected output as per the input.
