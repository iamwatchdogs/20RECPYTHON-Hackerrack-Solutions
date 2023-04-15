# Problem Statement:
# ------------------
# Kapple company has just released a latest model of KPhoneXI. There is a queue outside one of the stores and the store manager has decided for 2 giveaways to attract more customers. The giveaways will be given to the people who are in the queue.

# The store manager has asked the customers in the queue to pick a positive number of their choice. Manager finds the floor average of the numbers picked by them and prepares a shortlist of those who have chosen floor average as their number. He then identifies the winners having the maximum distance between them.

# Given an array of N positive integers, representing the numbers chosen by N customers in the queue, write a program to find out the distance between the winners. Print -1 if winners cannot be identified.

# Input Format:
# -------------
# First line of the input contains the number of customers, N. Second line of the input contains positive integers separated by spaces. Read the input from standard input.

# Sample Input 0:
# 7
# 5 3 2 5 3 2 3
# Sample Output 0:
# 5
# Explanation 0:
# Floor average of all the numbers present is 3. 
# Maximum distance between the people who has chosen 3 as their value is 5.

# Oneliner Solution:
print((lambda n,q: ((lambda l: (max(l) - min(l)))([i for i, x in enumerate(q) if x == sum(q)//n]) if q.count(sum(q)//n) > 1 else -1))(int(input()),list(map(int, input().split()))))

# My Solution:
n = int(input())
q = list(map(int, input().split()))
avg = sum(q)//n
val = (lambda l: (max(l) - min(l)))([i for i, x in enumerate(q) if x == avg]) if q.count(avg) > 1 else -1
print(val)

# Readiable Solution:
n = int(input())
q = list(map(int, input().split()))
avg = sum(q)//n
index = [i for i in range(len(q)) if q[i] == avg]
if q.count(avg) <= 1:
    print(-1)      
else:
    idxs = [i for i, x in enumerate(q) if x == avg]
    print(max(idxs) - min(idxs))
    
# Alternate Readiable Solution:
n = int(input())
q = list(map(int, input().split()))
avg = sum(q)//n
index = [i for i in range(len(q)) if q[i] == avg]
if q.count(avg) <= 1:
    print(-1)
elif q.count(avg) == 2:
    idx1 = q.index(avg)
    idx2 = q.index(avg, idx1 + 1)
    print(abs(idx1 - idx2))        
else:
    idxs = [i for i, x in enumerate(q) if x == avg]
    print(max(idxs) - min(idxs))

# My Friend's Solution: (2-Pointer Method)
x = int(input())
lst = list(map(int,input().split()))
aver = sum(lst)//len(lst)
i = 0
j = len(lst)-1
s = 0
while(i < j):
    if(lst[i] != aver and lst[j] != aver):
        i = i + 1
        j = j - 1
    elif(lst[i] == aver and lst[j] != aver):
        j = j - 1
    elif(lst[i] != aver and lst[j] == aver):
        i = i + 1
    else:
        s = j - i
        break
if(s == 0):
    print("-1")
else:
    print(s)
