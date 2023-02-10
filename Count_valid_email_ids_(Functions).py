# Problem Statement: Function to return count of valid email ids
#
# Constraints: Input should contain atlease one email-id
#
# Sample Input 0: uma@gmail.com shan@yahoo.com @gmail.com uma@for.co shankar@yahoo.com
# Sample Output 0: 3
#
# Sample Input 1: uma@ shankar@gmail.com @gmail.com yahoo@yahoo.com
# Sample Output 1: 2
    
# My Solution:
count=0
for i in input().split():
    if i[0] != '@' and i.endswith('@gmail.com') or i.endswith('@yahoo.com'):
        count += 1
print(count)

# Actual and best Solution:
import re

count = 0
emails = input().split()
for email in emails:
    if re.match("^[a-zA-Z0-9_.+-][a-zA-Z0-9_.+-]+@(gmail|yahoo).com$", email):
        count += 1

print(count)

# Note that 're' is a package/module in python used for parsing the token through Regular Expressions.
# The following RE says that the input string should begin with any number of alphanumeric characters
# and then followed by the '@' symbol. After '@' the string should contain set of character which say
# either 'gmail' or 'yahoo' then followed by '.' character and ends with the set of charater which say
# 'com'.
