# Problem Statement: Index of second largest element(lists)
#
# Sample Input 0: 12 78 34 56 89
# Sample Output 0: 1
#
# Sample Input 1: 49 56 23 78 87
# Sample Output 1: 3 
    
# My Solution:
l = list(map(int, input().split()))
temp = set(l)
temp.remove(max(temp))
print(l.index(max(temp)))

# Other possible solution:
l = list(map(int, input().split()))
temp = sorted(set(l), reverse=True)
print(l.index(temp[1]))
