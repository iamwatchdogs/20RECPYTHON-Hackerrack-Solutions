# Problem Statement: Uma shankar is a student of a class and he wants to calculate percentage and grade from a given scores
#
# Constraints:
#       List of Scores should be positive
#       Display Grade as given below conditions
#       percentage >= 75 (A)
#       percentage >= 60 and percentage < 75 (B)
#       percentage >= 50 and percentage < 60 (C)
#       percentage >= 35 and percentage < 50 (D)
#       percentage < 35 (E)
#
# Sample Input 0:
#       55 56 44 78 59 60
# Sample Output 0:
#       Percentage : 58.67
#       Grade : C
  
# My Solution:
l = list(map(int, input().split()))
s = sum(l)/len(l)
print("Percentage : {:.2f}".format(s))  # using round(s,2) fails one of the test cases
print('Grade :', end=' ')
if s >= 75:
    print('A')
elif s >= 60:
    print('B')
elif s >= 50:
    print('C')
elif s >= 35:
    print('D')
else:
    print('E')
