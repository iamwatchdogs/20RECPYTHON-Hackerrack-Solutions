# Problem Statement:
#     Given a sentence, write a program to print the encoded sentence based on the following rules: 
#         1. Promote all the upper case characters to their next 4th character in lower case in the cyclic alphabetical order  
#         2. Demote all the lower case characters to their previous 4th character in upper case in the cyclic alphabetical order 
#         Note : A, B, .....X, Y, Z, A, B... represents the cyclic order
#
# Sample Input 0:   Hello World
# Sample Output 0:  lAHHK aKNHZ
# Sample Input 1:   A Book holds a House of Gold
# Sample Output 1:  e fKKG DKHZO W lKQOA KB kKHZ
#
# Note: ord('A') = 65, ord('a') = 97

# My Solution:
res = ''
for i in input():
    val = i
    if i.isupper():
        val = chr((ord(i) - 65 + 4) % 26 + 65).lower()
    elif i.islower():
        val = chr((ord(i) - 97 - 4) % 26 + 97).upper()
    res += val
print(res)

# Best Solution:
res = ''
for i in input():
    val = i
    if i.isupper():
        val = chr((ord(i) - 65 + 4) % 26 + 97)
    elif i.islower():
        val = chr((ord(i) - 97 - 4) % 26 + 65)
    res += val
print(res)

# My Friend's Solution:
lst = input().split()
l1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s =""
for i in range(0,len(lst)):
    for j in range(0,len(lst[i])):
        if(lst[i][j].isupper()):
            s += (l1[(l1.index(lst[i][j]) + 4) % 26]).lower()
        else:
            s += l1[(l1.index(lst[i][j].upper()) - 4)]
    s += " "
print(s)
