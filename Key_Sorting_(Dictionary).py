# Problem Statement: Dictionary is a pair of key and value.now we want to sort the data in dictionary based on key.
#
# Sample Input 0:
#         80 krishna 60 abc 50 uma
# Sample Output 0:
#         50: uma
#         60: abc
#         80: krishna
# Sample Input 1:
#         10 20 50 70 40 20
# Sample Output 1:
#         10: 20
#         40: 20
#         50: 70

# My Solution: ( Might be the best ? )
l=input().split()
d={ l[i]:l[i+1] for i in range(0,len(l),2) }
for k in sorted(d):
    print(f'{k}: {d[k]}')
