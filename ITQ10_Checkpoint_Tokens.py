# Problem Statement:
#   Sam is participating in a vehicle rally which passes through various checkpoints where some tokens are kept. An array (T) of positive integers is given,
#   where each element represents the number of tokens available at each checkpoint. As Sam moves from one checkpoint (i) to the next (i+1), 
#   he gets T[i]-T[i+1] tokens for free if it is a positive integer otherwise he loses those many number of tokens. Since movement is allowed only if Sam has
#   non negative number of tokens, he has to buy additional tokens. Sam starts the rally with no tokens.
#
#   Write a program to calculate the total number of tokens Sam has to buy to reach the destination.
# 
#   Assume the tokens available are 10, 6, 11, 4, 2, 3. 
#   Tokens bought to reach the first checkpoint: 10 (0 – 10) Tokens bought to reach the second checkpoint: 0 ,
#   he gained 4 (10-6) Tokens bought to reach the third checkpoint: 1 (6 – 11 + 4) Tokens bought to reach the fourth checkpoint: 0,
#   he gained 7 and he reach the destination without buying any more Tokens. Hence the number of tokens bought is 11
# 
# Sample Input 0:   1,9,33,2,17,15,10,15,22,25
# Sample Output 0:  33

# My Solution:
l = list(map(int,input().split(','))) #10, 6, 11, 4, 2, 3
tokens_bought = l[0]
tokens_gained = 0
for i in range(1,len(l)):
    tokens_gained += l[i-1]-l[i]
    if tokens_gained < 0:
        tokens_bought += abs(tokens_gained)
        tokens_gained = 0
print(tokens_bought)

# My friend's Solution:
l=list(map(int,input().split(',')))
re=l[0]
av=0
for i in range(len(l)-1):
    if(l[i]-l[i+1]>=0):
        av+=l[i]-l[i+1]
    else:
        if av-(l[i+1]-l[i])<0:
            re+=av-(l[i]-l[i+1])
print(re)
