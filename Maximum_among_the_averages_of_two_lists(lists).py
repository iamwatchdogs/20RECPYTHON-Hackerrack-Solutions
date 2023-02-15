# Problem Statement:
#     Find average of list 1(avg1)
#     Find average of list 2(avg2)
#     Then find maximum among avg1 and avg2
#
# Sample Input 0:
#         1 2 3 4 5
#         2 4 6 8
# Sample Output 0:
#         5.0
#
# Sample Input 1:
#         2 2 2 2 2 
#         1 1 1 1 1 1 
# Sample Output 1:
#         2.0

# My Solution:
x = list(map(int, input().split()))
y = list(map(int, input().split()))
avg = lambda x: sum(x)/len(x)
print( avg(x) if avg(x) > avg(y)  else avg(y) )

# Alternative Solution:
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(sum(x)/len(x) if sum(x)/len(x) > sum(y)/len(y) else sum(y)/len(y))
