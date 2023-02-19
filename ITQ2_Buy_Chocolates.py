# Problem Statement: Uncle Mark wants to buy the costliest chocolate for all the kids. The kids demand for the same
#                    chocolate. The stock availability of chocolates, S in a store and the number of kids, N are given.
#                    Write a program to print the amount required to buy the chocolates. Print 0 if sufficient stock
#                    doesn’t exist.
#
# Input Format:
# First line contains the number of kids N
#
# Second line contains the stock availability details S details in the format 
# chocolate_name:price:quantity_available separated by comma.
#
# Sample Input 0:
#                   5
#                   Kinder:30:2,Cadbury:15:8
# Sample Output 0:
#                   75
# Explanation 0:
#                  ‘Kinder’ is the costliest chocolate but it is not sufficient for all the children. 
#                   Hence, ‘Cadbury’ is the next costliest chocolate which can be bought for all the children. 
#                   Hence the amount needed is 75.
#
# Sample Input 1:
#                   7
#                   Bournville:70:4,Pips:65:10,Perk:45:12
# Sample Out        put 1:
#                   455

# My Solution:
nok =int(input())
quantity = list()
price = list()
for i in input().split(','):
    quantity.append(int(i.split(':')[-1]))
    price.append(int(i.split(':')[-2]))
cost = [0] + [ nok*price[i] for i in range(len(quantity)) if quantity[i] >= nok ] 
print(max(cost))

# My Friend's Solution:
nok=int(input())
stock=input().split(",")
c=[]
quantity=[]
price=[]
for i in range(len(stock)):
    quantity.append(stock[i].split(":")[-1])
    price.append(stock[i].split(":")[-2])
for i in range(len(quantity)):
    if int(quantity[i])>=nok:
        t=(nok*int(price[i]))
        c.append(t)
try:
    print(max(c))
except:
    print("0")
