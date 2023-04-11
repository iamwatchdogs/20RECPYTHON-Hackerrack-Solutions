# Problem Statement:
#   Given a string S, write a function ‘findASCII’ to print the ASCII value of the character occurring maximum odd number of times.
# 
# Sample Input 0:   AABccdE
# Sample Output 0:  66
#
# Sample Input 1:   AAcAbbbbCACC
# Sample Output 1:  67

# My Solution:
def findASCII(s):
    m = { 'item': None, 'count': 0 }
    for i in s:
        c = s.count(i)
        if c > m['count'] and c%2 != 0:
            m['item'],m['count'] = i,c
    return ord(m['item'])

print(findASCII(input()))

# My friend's Solution:
def findASCII(s):
    count = 0
    c = None
    for i in s:
        x = s.count(i)
        if x%2 != 0 and x > count:
            c = i
            count = x
    return ord(c)
print(findASCII(input()))
