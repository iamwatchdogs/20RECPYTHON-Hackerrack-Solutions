# Problem Statement: create a funtion having the parameters like student name, rollno and average marks of all subjects. function can accept (functions)
#
# Sample Input 0:
#         krishna 12a 67
# Sample Output 0:
#         Name: krishna
#         Rollno: 12a
#         Avg: 67
#
# Sample Input 1:
#         shankar 15a
# Sample Output 1:
#         Name: shankar
#         Rollno: 15a
#         Avg: 35
    
# My Solution: ( Maybe the best Solution? )
def student ( name, rollno, avg = 35 ):
    print('Name:', name)
    print('Rollno:', rollno)
    print('Avg:', avg)
    
l = input().split()
student(l[0],l[1],l[2]) if len(l) == 3 else student(l[0], l[1])
