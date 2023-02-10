# Problem Statement: Unzip a list of tuples into individual lists
#
# Sample Input 0 : 10 20 30 40 50 60
# Sample Output 0 : [(10, 30, 50), (20, 40, 60)]

# My solution:
l=list(map(int,input().split()))
res=list()
res.extend([tuple([l[i] for i in range(0,len(l),2)])])
res.extend([tuple([l[i] for i in range(1,len(l),2)])])
print(res)

# Best solution:
l = list(map(int, input().split()))
res = [tuple(l[0::2]), tuple(l[1::2])]
print(res)
