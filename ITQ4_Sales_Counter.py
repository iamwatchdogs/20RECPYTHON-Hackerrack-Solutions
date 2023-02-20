# Problem Statement:
#   Max is a baker whose snacks are very popular in the town. Max sells only one item per person in a day to serve
#   maximum customers. To keep a tab on the sales, Max writes the items sold in his ledger. Given a string S, containing
#   the names of snacks sold by Max in a day, write a python function ‘maxSales’ to print the item purchased by the 
#   maximum number of customers. If more than one such item exists, then print the item with the shortest name.
#
# Sample Input 0:
#               hotdog,fries,hotdog,burger,cheese pizza,burger,fries,hotdog
#               Sample Output 0: 
# hotdog:3
# Explanation 0: 
#               hotdog is sold maximum number of times
#
# Sample Input 1: 
#               hotdog, fries, cheese pizza, burger, cheese pizza, burger, fries, cheese pizza, fries, chicken pizza, 
#               burger, cheese pizza
# Sample Output 1: 
#               cheese pizza:4
# Explanation 1: 
#               cheese pizza is sold maximum number of times

# My Solution:
def maxSales(s):
    s = list(s.split(','))
    ledger = { i.strip():s.count(i) for i in s }
    max_val = max(ledger, key=lambda k: ledger[k])
    print(f'{max_val}:{ledger[max_val]}')

maxSales(input())   

# My Friend's Solution:
snack=input().split(",")
l=[i.lstrip() for i in snack]
myd={}
for i in l:
    if i not in myd:
        myd[i]=l.count(i)
t=max(myd.values())
for k,v in myd.items():
    if v==t:
        print(k,":",v,sep="")
        break
