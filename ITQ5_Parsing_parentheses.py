# Problem Statement:
#   Given an arithmetic expression with parentheses, write a program to print the sequence of opening and closing of
#   parentheses. For example, consider the following expression: (a + b)(5(c - d)) Paranthesis 1 opens Paranthesis 1 
#   closes Paranthesis 2 opens Paranthesis 3 opens Paranthesis 3 closes Paranthesis 2 closes Hence, the sequence will be:
#   112332
#
# Sample Input 0: (5+(t*(10-6)))+(8+f)
# Sample Output 0: 12332144
# Explanation 0: 
#   In the sample input first parentheses starts at the first index before 5, so print 1. Second parentheses start before
#   t, so print 2. Third parentheses start before 10, so print 3. Third parentheses end after 6, so print 3. Second
#   parentheses end after the end of third parentheses, so print 2, and so on.

# My Solution:
k = 1
stack = list()
for i in input():
    if i == '(':
        stack.append(k)
        print(k,end='')
        k += 1
    elif i == ')':
        print(stack.pop(),end='')
        
