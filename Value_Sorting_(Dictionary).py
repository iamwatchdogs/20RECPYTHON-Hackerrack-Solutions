# Problem Statement: To sort the different subject marks (Dictionary)
#
# Sample Input 0:
#          maths 20 science 10 english 3
# Sample Output 0:
#          english 3
#          science 10
#          maths 20
# Sample Input 1:
#          a 100 b 40 c 30 d 43 f 40
# Sample Output 1:
#          c 30
#          b 40
#          f 40
#          d 43

# My Solution:
l = input().split()
d = { l[i] : int(l[i+1]) for i in range(0,len(l),2) }
l = sorted(d,key=d.get)
for k in l:
    print(k,d[k])
    
# Best Solution:
l = input().split()
d = { l[i]: int(l[i+1]) for i in range(0, len(l), 2) }
for k, v in sorted(d.items(), key=lambda item: item[1]):
    print(k, v)
