# Problem Statement:
#     Write a program to check if the number is an abundant number. 
#     A number is said to be abundant if the sum of proper divisors is greater than the number itself.
#
# Sample Input 0:  12
# Sample Output 0: True
# Explanation 0:   12 is an abundant number
#
# Sample Input 1:  121
# Sample Output 1: False
# Explanation 1:   121 is not an abundant number


# My One-liner solution:
print((lambda n: sum([ i for i in range(1,n//2+1) if n%i == 0]) > n)(int(input())))

# My Solution:
n = int(input())
s = sum([ i for i in range(1,n//2+1) if n%i==0 ])
print(s > n)

# My Friend's Solution:
n=int(input())
l=0
for i in range(1,n//2+1):
    if n%i==0:
        l+=i
if l>n:
    print("True")
else:
    print("False")
