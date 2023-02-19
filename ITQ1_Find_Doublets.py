# Problem Statement: Given an alphabetic string, write a program to print the unique doublets. Print -1 if no doublets
#                    are found. A doublet is a pair of words that differ by exactly one letter.Eg:‘booster’ and rooster’.
#
# Sample Input 0:
#                   toaster
#                   boaster
#                   boastel
#                   coaster
#                   postal
# Sample Output 0:
#                   toaster:boaster,toaster:coaster,boaster:boastel,boaster:coaster
# Explanation 0:
#                   Each of the doublets separated by comma differ exactly by one character

# Sample Input 1:
#                   boxstar
#                   boaster
#                   boestel
#                   coalter
#                   postal
# Sample Output 1:
#                   -1
# Explanation 1:
#                   There are no doublets in the given sentence and hence -1


# My Solution:
import sys
l =  [ i.strip() for i in sys.stdin.readlines() ]

def is_doublets(a,b):
    return len(a) == len(b) and len([ i for i in range(len(a)) if a[i] != b[i]]) == 1
  

res= [ str(l[i])+':'+str(l[j]) for i in range(len(l)) for j in range(i+1,len(l)) if is_doublets(l[i],l[j]) ]

print( '-1' if len(res) == 0 else ''.join( [ res[i]+',' for i in range(len(res)-1) ] )+res[len(res)-1] )

# My Friend's Solution:
l=[]
while True:
    try:
        l.append(input())
    except:
        break

def func1(a,b):
    if len(a)!=len(b):
        return False
    else:
        c=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        if c==1:
            return True
        return False
c=0
res=list()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if func1(l[i],l[j])==True:
            res.append(str(l[i]+":"+str(l[j])))
if len(res)!=0:
    for i in range(len(res)-1):
        print(res[i],end=",")
    print(res[-1])
else:
    print("-1")
