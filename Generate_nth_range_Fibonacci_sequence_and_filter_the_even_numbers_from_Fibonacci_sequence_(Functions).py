# Problem Statement : Function to generate nth range Fibonacci sequence and
#                     filter the even numbers from Fibonacci sequence.
#                     (Hint : use filter() function with lambda)
#
# Constraints: Number should be positive
#
# Sample Input 0: 15
# Sample Output 0: 
#     Fibonacci Sequence :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
#     Even numbers from Fibonacci Sequence : [0, 2, 8, 34, 144]
# Sample Input 1:-7
# Sample Output 1:
#     Invalid input : Number should be positive
    
# My Solution
n=int(input())
if n < 0 :
    print('Invalid input : Number should be positive')
else:
    fib=[0,1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    print('Fibonacci Sequence : ', fib)
    print('Even numbers from Fibonacci Sequence :', [ i for i in fib if i % 2 == 0] )
    
# Actual and best Solution:
n=int(input())
if n < 0:
    print('Invalid input : Number should be positive')
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    print('Fibonacci Sequence : ', fib)
    print('Even numbers from Fibonacci Sequence :', list(filter(lambda x: x % 2 == 0, fib)) )
    
# filter method syntax: filter(function, iterable)
# filter() returns an object filters by the provided function from the given iterable.
