# Problem Statement: To copy prime numbers in to another list (Lists)
#
# Constraints: List of elements should be positive
#
# Sample Input 0: 2 8 3 11 24 7 44
# Sample Output 0: [2, 3, 11, 7]
    
# My Original Solution:
print( [ i for i in list(map(int,input().split())) if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1)) ] )

# Alternative Solution:
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print( [ i for i in list(map(int,input().split())) if is_prime(i) ])

# My Solution ( More Readable ):
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if (n % i == 0):
                return False
    return True

l = list(map(int, input().split()))
print( [ i for i in l if is_prime(i) ] )

# Original Best Solution [Fermat's Little Theorem]: O(1)
print( [ i for i in list(map(int,input().split())) if i >= 2 and (2**i-1)%i == 1 ] )

# Best Solution ( More Readable ):
def is_prime(n):
    if n <= 1:
        return False
    else:
        p = (2**n-1)%n
        return p == 1
      
l = list(map(int, input().split()))
print( [ i for i in l if is_prime(i) ] )
