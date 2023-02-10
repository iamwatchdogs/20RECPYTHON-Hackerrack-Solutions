# Problem Statement: Deleting keys with duplicate values
#
# Constraints: Dictionary should not be empty
#
# Sample Input 0: eng 66 m1 54 m2 44 phy 54 che 37 cp 44
# Sample Output 0: eng 66 che 37
#
# Sample Input 1: eng 68 m1 89 m2 94 phy 54 che 66 cp 44
# Sample Output 1: eng 68 m1 89 m2 94 phy 54 che 66 cp 44

# ------------------ My Solution ----------------------------

l = input().split()
d = { l[i]:l[i+1] for i in range(0,len(l),2) }
x = list(d.values())
rv = list()
for i in x:
    if x.count(i) > 1:
        rv.append(i)
for k,v in d.items():
    if (v not in rv): 
        print(k, v, end = " ")

# ------- My friend's Solution ( even better ) -------------

l = input().split()
d = {l[i]:l[i+1] for i in range(0,len(l),2)}
nd = d.copy()
for k in d:
    if l.count(d[k]) > 1:
        del nd[k]
for k in nd:
    print(k, d[k], end = " ")
    
# ----------------- Best Solution ---------------------------

l = input().split()
d = {l[i]: l[i + 1] for i in range(0,len(l),2)}
duplicates = set()
for k, v in d.items():
    if l.count(v) > 1:
        duplicates.add(v)
for k, v in d.items():
    if v not in duplicates:
        print(k, v, end=" ")
