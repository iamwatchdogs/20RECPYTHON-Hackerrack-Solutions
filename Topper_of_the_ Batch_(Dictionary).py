# Problem Statement: There are some students in a class. Each student having some marks for each subject.
#                    and finally teacher wants to know who is the topper of the class(Dictionary)
#
# Constraints: marks should not be negitive and not more than 100
#
# Sample Input 0:
#       a1 a2 a3
#       s1 20 s2 40 s3 50
#       s1 40 s2 50 s3 60
#       s1 20 s2 60 s3 80
# Sample Output 0:
#       a3 160
# Sample Input 1:
#       krishna uma koushik
#       m1 100 m2 60 m3 40
#       m1 30 m2 50 m3 70
#       m1 100 m2 90 m3 80
# Sample Output 1:
#       koushik 270

# My Solution: ( Might be the best ? )
d={}
l=input().split()
for i in l:
    d[i]=sum(list(map(int,list(input().split()[1::2]))))
k=max(d,key=d.get)
print(k,d[k])
