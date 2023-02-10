tement: dictionary is pair of key and a value. now we want to delete unnecessary pairs from the dictionary.
#
# Sample Input 0: 
#         a 10 b 20 c 30
#         a
# Sample Output 0:
#         b: 20
#         c: 30
# Sample Input 1:
#         a 10 b 20 c 30
#         d
# Sample Output 1:
#         Given key is not in the dictionary

# My Solution:
l=input().split()
d={ l[i] : l[i+1] for i in range(0,len(l),2) }
c=input()
if c in d.keys():
    del d[c]
    for k,v in d.items():
        print(f"{k}: {v}")
else:
    print("Given key is not in the dictionary")
    
# Best Solution:
l=input().split()
d={ l[i] : l[i+1] for i in range(0,len(l),2) }
c=input()
if c in d.keys():
    del d[c]
    print("\n".join([f"{k}: {v}" for k,v in d.items()]))
else:
    print("Given key is not in the dictionary")
