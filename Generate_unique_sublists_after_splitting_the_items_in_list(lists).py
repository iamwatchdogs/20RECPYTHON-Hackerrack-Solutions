# Problem Statement: To generate unique sublists after splitting the items in list
#
# Sample Input 0: abc bcd def
# Sample Output 0: [['a'], ['b'], ['c'], ['d'], ['e'], ['f']]
#
# Sample Input 1: hai cse ece
# Sample Output 1: [['h'], ['a'], ['i'], ['c'], ['s'], ['e']]

# My Solution:
l = list(input().replace(' ',''))
temp = list()
for i in l:
    if list(i) not in temp:
        temp.append(list(i))
print(temp)

# Best Solution:
l = list(input().replace(' ', ''))
temp = []
[ temp.append([i]) for i in l if [i] not in temp ]
print(temp)

# Best Possible Solution: ( but won't pass the test cases )
print( [ list(i) for i in set(list(input().replace(' ',''))) ] )
