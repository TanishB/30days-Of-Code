import math
num = int(input())
array = []
for i in range(num):
    temp = int(input())
    array.append(temp)
    
def isPrime(n):
    if n <= 1:
        return False
    sqrtN = math.sqrt(n)
    if sqrtN.is_integer():
        return False
    
    for i in range(2,int(sqrtN) + 1):# Adding 1 in case it rounds down
        if n%i == 0:
            return False
    return True

for n in array:
    
    if isPrime(n):
        print('Prime')
    else:
        print('Not prime')

'''
UnOptimised Solution:

num = int(input())
array = []
for i in range(num):
    temp = int(input())
    array.append(temp)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for n in array:
    
    if isPrime(n):
        print('Prime')
    else:
        print('Not prime')
'''