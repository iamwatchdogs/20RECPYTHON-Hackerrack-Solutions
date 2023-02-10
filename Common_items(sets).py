# Problem Statement: A and B went to market for buying daily vegetables individually.
#                    after returning to the home they checked out which items were similar.(lists)
#
# Constraints: both lists should not be empty
#
# Sample Input 0:
#       Red Green Orange White Green White
#       Black Green White Pink White
# Sample Output 0:
#       ['Green', 'White']
# Sample Input 1:
#       Red Green Orange White
#       Black Pink
# Sample Output 1:
#       []

# My Solution:
a = input().split()
b = input().split()
res = [i for i in set(a).intersection(set(b))]
res.sort()
print(res)

# Best Solution:
a = set(input().split())
b = set(input().split())
res = sorted(list(a & b))
print(res)
