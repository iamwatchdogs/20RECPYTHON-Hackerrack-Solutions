# Problem Statement:
#   Mat manages Livingston Library. He uses a unique numbering pattern for books gifted by the members. 
#   Each book will have a unique alphabet sequence followed by a 4-digit numeric sequence. 
#   Alphabet sequence: A,B … Z, AA, AB … ZZ, AAA … ZZZ … 
#   Number Sequence: 0001 to 9999 
#   Sample Book ID: A0001, A0002,…..,A9999, B0001,….Z9999,AA0001....ZZ9999,...
#   Given the last generated book ID and the number of new books gifted by the members, write a program to print the book IDs.
#
# Sample Input 0:
#   Z9998
#   5
# Sample Output 0:
#   Z9999,AA0000,AA0001,AA0002,AA0003

# My Solution:
l=[input()]
for i in range(int(input())):
    split=0
    while l[i][split].isalpha():
        split += 1
    h, b = l[i][:split], l[i][split:]
    
    if all( j == '9' for j in b ):
        b = ''.join( [ '0' for _ in range(len(b)+1)] )
        if all( k == 'Z' for k in h ):
            h = ''.join( [ 'A' for _ in range(len(h)) ] )
            b = 'A' + b[1:]
        elif h[-1] == 'Z':
            s = 1
            while h[s] != 'Z':
                s += 1
            h = str(h[:s-1])+chr(ord(h[s-1])+1)+''.join( [ 'A' for _ in range(len(h[s:])) ] )
    else:
        padding_zeros = len(b)
        b = str(int(b)+1)
        b = ''.join( [ '0' for _ in range(padding_zeros-len(b)) ] ) + b
    l.append(h+b)
print(','.join(l[1:]))

# Best Solution:
inputs = [input()]
for i in range(int(input())):
    split = 0
    while inputs[i][split].isalpha():
        split += 1
    h, b = inputs[i][:split], inputs[i][split:]
    
    if all(j == '9' for j in b):
        b = '0' * (len(b) + 1)
        if all(k == 'Z' for k in h):
            h = 'A' * len(h)
            b = 'A' + b[1:]
        elif h[-1] == 'Z':
            s = 1
            while h[s] != 'Z':
                s += 1
            h = h[:s-1] + chr(ord(h[s-1]) + 1) + 'A' * len(h[s:])
    else:
        padding_zeros = len(b)
        b = str(int(b) + 1)
        b = '0' * (padding_zeros - len(b)) + b
    inputs.append(h + b)
print(','.join(inputs[1:]))
