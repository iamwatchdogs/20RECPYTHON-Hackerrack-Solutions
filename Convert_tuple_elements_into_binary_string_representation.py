# Probelm Statement: Convert a tuple elements in to binary string representation
#
# Constraints: tuple should contains only positive integers
#
# Sample Input 0: 15 9 6 8 22 56
# Sample Output 0: ('0b1111', '0b1001', '0b110', '0b1000', '0b10110', '0b111000')
#
# Sample Input 1: 34 -56 44 88
# Sample Output 1: Invalid Operation : tuple should not contain negative numbers

# My solution:
l = list(map(int, input().split()))
flag = True
for i in l:
    if i < 0:
        flag = False
if flag:
    print(tuple(map(bin, l)))
else:
    print("Invalid Operation : tuple should not contain negative numbers")

# Best Solution:
input_list = list(map(int, input().split()))
print( tuple(map(bin, input_list)) if all(i >= 0 for i in input_list) else "Invalid Operation : tuple should not contain negative numbers" )

# The regular if-else statements are replaced by the ternary operator, the all() checks thought the itereation and
# the map() function maps the input to bin() which give the equivalent binary representation.
   
