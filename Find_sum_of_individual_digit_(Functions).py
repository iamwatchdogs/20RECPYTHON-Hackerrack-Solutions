# Problem Statement: Function to accept list of integer as an argument and find sum of individual digit.
#
# Hint : use map() function with lambda
#
# Constraints: Numbers should be positive
#
# Sample Input 0: 13 254 11
# Sample Output 0: [4, 11, 2]
#
# Sample Input 1: 2 5 9 6
# Sample Output 1: [2, 5, 9, 6]
    
# ---------------- My Original Solution: ---------------------------
def sum_of_digits ( n ):
    num = 0
    while n > 0:
        num += n%10
        n //= 10
    return num
print(list(map(lambda a : sum_of_digits(a), list(map(int,input().split())))))

# ---------------- My Solution (Readable): -------------------------
def sum_of_digits ( n ):
    num = 0
    while n > 0:
        num += n%10
        n //= 10
    return num

l = list(map(int,input().split()))
res = list(map(lambda a : sum_of_digits(a), l))
print(res)

# ---------------------- Best Solution: ----------------------------
print(list(map(lambda x: sum(int(i) for i in str(x)), list(map(int, input().split())))))

# ---------------- Best Solution (Readable): -----------------------
def sum_of_digits ( n ):
    return sum(int(digit) for digit in str(n))

l = list(map(int, input().split()))
res = list(map(lambda x:sum_of_digits(x), l))
print(res)
