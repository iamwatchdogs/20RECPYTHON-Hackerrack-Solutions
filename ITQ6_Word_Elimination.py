# Problem Statement:
  
#   Given a natural number N and a sentence S of length L, contaning W words ,
#   write a program to print the sentence after eliminating a word as per the below rules:
#     1. Calculate C, the number of occurences of the character at Nth index of S 
#     2. Consider the last character for calculating C if N >= L 
#     3. Eliminate word at Cth position from S. 
#   Eliminate the last word if C > W

# Constraints: W>1 Use case sensitive comparison wherever needed

# Sample Input 0:
#   I am a good boy
#   2
# Sample Output 0:
#   I a good boy
  
# Explanation 0:
#   The character present in index 2 is 'a'. 
#   It appears twice in the in the message. 
#   So the word at second position in the message 'am' is removed

# Sample Input 1:
#   I am a good boy
#   300
# Sample Output 1:
#   am a good boy
# Explanation 1:
#   Here 300 is greater than the length of the sentence. 
#   So the character at the last index which is 'y' is taken for counting. 
#   'y' appears only once in the message. So the word at the first position 'I' is removed.
  
# My Solution:
s = input()
n = int(input())
count = s.count(s[n]) if n < len(s) else s.count(s[-1])
t = s.split()
t.pop( (count-1) if count < len(t) else -1 )
print(' '.join(t))

# My friend's Solution:
sen=input()
w=sen.split()
n=int(input())
if n>=len(sen):
    n=len(sen)-1
c=sen.count(sen[n])
if c>len(w):
    del w[-1]
else:
    del w[c-1]
for i in w:
    print(i,end=" ")
