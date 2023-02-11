# Problem Statement: Crete new list by finding Sum of individual digit operation on each element of a list (Lists)
#
# Constraints: List elements should be positive
#
# Sample Input 0: 10 232 45 
# Sample Output 0: [1, 7, 9]
    
# My Original Solution:
print(list(map(lambda x:sum(int(i) for i in str(x)), list(map(int,input().split())))))

# My Solution ( Readable ):
def sum_of_digits ( n ):
    return sum(int(digit) for digit in str(n))

l = list(map(int, input().split()))
res = list(map(lambda x:sum_of_digits(x), l))
print(res)

# Alternative Solution:
def sum_of_digits ( n ):
    num = 0
    while n > 0:
        num += n%10
        n //= 10
    return num
print(list(map(lambda a : sum_of_digits(a), list(map(int,input().split())))))
