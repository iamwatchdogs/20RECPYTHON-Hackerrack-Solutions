# Problem Statement: Function to accept list of integer and filter numbers that contains even digit in units place.
#
# Hint: use filter() function with lambda (or) create user defined function
#
# Constraints: Numbers should be positive
#
# Sample Input 0: 423 44 25 36 73 5555
# Sample Output 0: [423, 25, 73, 5555]
#
# Sample Input 1: 4 7 8 9 3 1 6
# Sample Output 1: [7, 9, 3, 1]

# My Original Solution:
print( [ i for i in list(map(int,input().split())) if (i%10) % 2 != 0 ] )

# My Solution ( More Readable ):
l = input().split()
l = list(map(int, l))
res = [ i for i in l if ( i % 10 ) % 2 != 0 ]
print(res)

# Actual Solution:
l = input().split()
l = list(map(int, l))
res = list(filter(lambda x: (x % 10)% 2 != 0, l))
print(res)

# Best Solution:
print(list(filter(lambda x: x % 2 != 0, list(map(int, input().split())))))

# filter method syntax: filter(function, iterable)
# filter() returns an object filters by the provided function from the given iterable.
