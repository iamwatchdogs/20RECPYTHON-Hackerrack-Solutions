# Problem Statement: Function that filters numbers which are divisible by 2 and 3
#
# Constraints: Input should be integer and it should be greater than zero
#
# Sample Input 0: 30
# Sample Output 0: [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]
#
# Sample Input 1: -5
# Sample Output 1: Invalid input : n>0

# My Solution:
n = int(input())
print('Invalid input : n>0' if n < 0 else [i for i in range(1,n)if i%2!=0 and i%3!=0])

# Actual and best Solution:
n = int(input())
print('Invalid input : n>0' if n < 0 else  list(filter(lambda x: x % 2 != 0 and x % 3 != 0, range(1, n + 1))))

# filter method syntax: filter(function, iterable)
# filter() returns an object filters by the provided function from the given iterable.
