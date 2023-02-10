# Problem Statement:
#   Find total salary of an employees after increment as given below conditions.
#       Increment : 50% if salary<5000
#       Increment : 30% if salary>=5000 and salary<=15000
#       Increment : 20% if salary>15000 and salary<=25000
#       Increment : 10% if salary>25000
#
# Constraints: Dictionary items should not be empty
#
# Sample Input 0:
#         uma 2000 shan 5000 cha 12000
# Sample Output 0:
#         uma : 3000
#         shan : 6500
#         cha : 15600
#
# Sample Input 1:
#         shankar 2000 uma 16000 umashankar 27000
# Sample Output 1:
#         shankar : 3000
#         uma : 19200
#         umashankar : 29700

# My Solution:
l = input().split()
d = { l[i]:int(l[i+1]) for i in range(0,len(l),2) }
for k,v in d.items():
    if v > 25000:
        d[k] = v+(v/10)
    elif v > 15000:
        d[k] = v+(v/5)
    elif v >= 5000:
        d[k] = v+(v*3/10)
    else:
        d[k] = v+(v/2)
for k,v in d.items():
    print(f"{k} : {int(v)}")
    
# Best Solution:
l = input().split()
d = { l[i]: int(l[i+1]) for i in range(0, len(l), 2) }
for k, v in d.items():
    if v <= 2500:
        d[k] = v * 1.5
    elif v <= 15000:
        d[k] = v * 1.3
    elif v <= 25000:
        d[k] = v * 1.2
    else:
        d[k] = v * 1.1
for k, v in d.items():
    print(f"{k} : {int(v)}")
