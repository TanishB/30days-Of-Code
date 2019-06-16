fullList = []
for i in range(6):
    tempList = []
    element = input().split(' ')
    for e in element:
        tempList.append(int(e))
    fullList.append(tempList)
sumList = []
for i in range(6-2):
    for j in range(6-2):
        #print(fullList[i][j])
        #print(fullList[i][j],fullList[i][j+1],fullList[i][j+2])
        #print('  ',fullList[i+1][j+1])
        #print(fullList[i+2][j],fullList[i+2][j+1],fullList[i][j+2])
        suum = fullList[i][j]+fullList[i][j+1]+fullList[i][j+2]+fullList[i+1][j+1]+fullList[i+2][j]+fullList[i+2][j+1]+fullList[i+2][j+2]
        sumList.append(suum)

print(max(sumList))
