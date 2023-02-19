# Probelm Statement: Jeany has a list of items but he is confused about how to find the unique items from the list.
#
# Sample Input 0: 10 20 10 30 10 20 40
# Sample Output 0: [30, 40]

# My Solution:
l = list(map(int,input().split()))
print( [ i for i in l if l.count(i) == 1 ])
