num = int(input())
consecutiveOne = 0
maxOne = 0
l=[]
while(num>0):
    rem = num % 2
    l.append(rem)
    if rem == 1:
        consecutiveOne += 1
        if consecutiveOne > maxOne:
            maxOne = consecutiveOne
    else:
        consecutiveOne = 0
    
    num = num // 2
    
print(maxOne)
    
'''
Conversion :

leng = len(l)
for i in range(leng-1,-1,-1):
    print(l[i])
'''
'''
ShortCut to convert number to binary
# bin(number)
eg: bin(5)

Converting binary
# int('number' , baseOfNumber)
eg: int('101' , 2 ) will give you 5
'''
