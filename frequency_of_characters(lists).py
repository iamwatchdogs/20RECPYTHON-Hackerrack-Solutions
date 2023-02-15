# Problem Statement: Paul has a list consisting of set of items. He wants to know how many times each item occured in the list
#
# Sample Input 0: a b c d a b c
# Sample Output 0: ('a', 2)('b', 2)('c', 2)('d', 1)
    
# My Original Solution:
s = input().replace(' ','')
d = { i:s.count(i) for i in s }
for x,y in d.items():
    print(f"('{x}', {y})",end="")
    
# Alternative Solution:
s = ''.join(input().split())
for x,y in { i:s.count(i) for i in s }.items():
    print(f"('{x}', {y})",end="")
    
# Best Solution:
s = ''.join(input().split())
print( ''.join( [ "('"+str(x)+"', "+str(y)+')' for x,y in { i:s.count(i) for i in s }.items()  ] ) )
