# Problem Statement: To check whether a number is perfect or not.(functions)
#
# Sample Input 0: 6
# Sample Output 0: True
#
# Sample Input 1: 8
# Sample Output 1: False

# My Solution: ( Maybe the best solution? )
def isperfect (n):
    sum=0
    for i in range(1,n):
        if n%i == 0:
            sum+=i
    print(sum == n)
isperfect(int(input()))
