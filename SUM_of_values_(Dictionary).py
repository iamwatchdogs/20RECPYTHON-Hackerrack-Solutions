# Problem Statement: Dictinary having a key and value pair, to find the sum of all values in a dictionary
#
# Sample Input 0: name 23 ss 44
# Sample Output 0: 67
#
# Sample Input 1: krishna 45 uma 78
# Sample Output 1: 123

# My Solution:
l=input().split()
d={ l[i]:int(l[i+1]) for i in range(0,len(l),2) }
s=0
for i in d.values():
    s += i
print(s)

# Best Solution:
l = input().split()
d = {l[i]: int(l[i+1]) for i in range(0, len(l), 2)}
print(sum(d.values()))
