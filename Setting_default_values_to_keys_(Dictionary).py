# Problem Statement: Coverting a list of items in to dictionary items
#
# Constraints: List should not be empty
#
# Sample Input 0: key1 key2 key3
# Sample Output 0: key1 0 key2 0 key3 0
#
# Sample Input 1: Key1 12R7503 501
# Sample Output 1: Key1 0 12R7503 0 501 0

# My Solution:
res={ i:0 for i in input().split() }
for i in res.keys():
    print( i,res[i],end=" " )
    
# Best Solution:
res = dict.fromkeys(input().split(), 0)
print(" ".join("{} {}".format(k, v) for k, v in res.items()))

# The dict.fromkeys() is used here creates a dictionary with the keys from the input and all values set to 0.
# " ".join() creates a string from the items in the dictionary, as "key value"
