phoneBook = {}
numberOfentries = int(input())
for i in range(numberOfentries):
    tempInput = input().split(' ')
    name = tempInput[0]
    number = int(tempInput[1])
    phoneBook[name] = number

queryList = []
while(1):
    try:
        query = input()
        queryList.append(query)
    except:
        break
    


for q in queryList:
    #print(q)
    if q in phoneBook:
        print(q,end='')
        print('=',end='')
        print(phoneBook[q])
    else:
        print('Not found')
