# Problem Statement:
#   Given a message containing words, write a program to print the encoded message according to the below rules: 
#   1. Write the words one below the other to form a 2D matrix and identify the largest word 
#   2. Fill the empty places with the sum of ASCII values of the characters in the current and 
#      previous column of the largest word 
#   3. Generate the encoded message by combining the elements column wise
#
# Example : 
#   Input Message :  "I AM A SPY" Largest Word : SPY Matrix Representation :
#
#           I           -           -
#           A           M           -
#           A           -           -
#           S           P           Y
#
#   Fill the empty cells:
#
#           I           ASCII(S)+ASCII(P) = 163         ASCII(P)+ASCII(Y) = 169
#           A           M                               ASCII(P)+ASCII(Y) = 169
#           A           ASCII(S)+ASCII(P) = 163         ASCII(P)+ASCII(Y) = 169
#           S           P                               Y
#
#   Final Matrix:
#
#           I           163                 169
#           A           M                   169
#           A           163                 169
#           S           P                   Y
#
#   Final Encoded Message : IAAS163M163P169169169Y
#
# Sample Input 0: I AM A SPY
# Sample Output 0: IAAS163M163P169169169Y

# My Solution:
l = list(input().split())
max_len_word = l.index(max(l))
for i in range(len(l[max_len_word])):
    for j in range(len(l)):
        try:
            print(l[j][i],end='')
        except:
            print(ord(l[max_len_word][i])+ord(l[max_len_word][i-1]),end='')

# My Friend's Solution:
l=list(input().split())
x=len(max(l))
s=""
c1=0
n=len(l)
for i in range(0,len(l)):
    if len(l[i])==x:
        c1=i
for i in range(x):
    for j in range(n):
        try:
            s+=str(l[j][i])
        except:
            s+=str(ord(l[c1][i])+ord(l[c1][i-1]))
print(s)
