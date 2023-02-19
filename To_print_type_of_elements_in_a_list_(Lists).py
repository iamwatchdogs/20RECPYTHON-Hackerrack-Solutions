# Problem Statement: To print type of elements in a list
#
# Constraints: List should not be empty
#
# Sample Input 0: 10 uma 3+4j 22.34 m
# Sample Output 0: ['int', 'str', 'complex', 'float', 'str']

# My Solution:
l = list()
for i in input().split():
    try:
        l.append(type(eval(i)).__name__)
    except:
        l.append('str')
print(l)
