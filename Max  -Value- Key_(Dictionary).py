# Problem Statement: To find the key index of max value of a dictionary (Dictionary)
#
# Sample Input 0: maths 85 science 35 social 45
# Sample Output 0: maths
#
# Sample Input 1: a 42 b 42 c 42 d 42
# Sample Output 1: a

# My Solution:
l=input().split()
d={ l[i]:l[i+1] for i in range(0,len(l),2) }    
m=max(d.values())
for k,v in d.items():
    if v==m:
        print(k)
        break
        
# Best Solution:
l=input().split()
d={ l[i]:l[i+1] for i in range(0,len(l),2) }    
m = max(d, key=d.get)
print(m)

# '.get' is a method that retrieves the value of a key in the dictionary. 
# So when we pass 'd.get' to the key argument, the max function will extract the values
# of the keys in the dictionary and compare them to find the maximum value.
