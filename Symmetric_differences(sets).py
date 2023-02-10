# Problem Statement: A and B went to supermarket purchasing some items. now print only A itmes or
#                    only print only B items but not both.(sets)
#
# Sample Input 0:
#           1 2 3 4 5
#           4 2 7 8 9
# Sample Output 0:
#           [1, 3, 5, 7, 8, 9]
# Sample Input 1:
#           apple orange mango banana
#           grape orange banana guava
# Sample Output 1:
#           ['apple', 'mango', 'grape', 'guava']

# My Solution:
a=input().split()
b=input().split()
res= [ i for i in a if i not in b] + [ j for j in b if j not in a ]
try:
    print(list(map(int,res)))
except:
    print(res)
    
# Best Solution: ( efficient memory usage )
a = input().split()
b = input().split()

res = []
for i in a:
    if i not in b:
        res.append(i)
for j in b:
    if j not in a:
        res.append(j)

try:
    res = list(map(int, res))
except ValueError:
    pass

print(res)
