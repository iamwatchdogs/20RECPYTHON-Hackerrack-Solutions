# Problem Statement:
#   Given an input string, write a program to print the length of the longest prefix which is also the suffix of the given string. 
#   The prefix and suffix should not overlap. Print 0 if no such suffix and prefix exists.
#
# Sample Input 0:    aabcdaabc
# Sample Output 0:   4
# Explanation 0:     The sub-string "aabc" is the longest prefix which is also suffix

# My Solution:
s = input()
res = max([ len(s[:i]) for i in range(len(s)//2+1) if s.endswith(s[:i]) ])
print(res)

# My One-Liner Solution:
print((lambda s: max([ len(s[:i]) for i in range(len(s)//2+1) if s.endswith(s[:i]) ]))(input()))

# My Friend's Solution:
s = input()
count = 0
for i in range(1,len(s)//2+1):
    if s.endswith(s[:i]):
        count = len(s[:i])
print(count)
