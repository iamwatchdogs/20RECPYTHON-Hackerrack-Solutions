# Problem Statement: Function to find the square of the two numbers and
#                    returns these values to the calling function and display it.
#    
# Sample Input 0:
#          2 3
# Sample Output 0:
#          4
#          9
#
# Sample Input 1:
#          5 8
# Sample Output 1:
#          25
#          64

# My Solution: ( Maybe the best solution? )
for i in ( map( lambda a: a**2, list(map(int,input().split())) ) ):
    print(i)
