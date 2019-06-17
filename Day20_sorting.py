n = int(input())
arr = input().split(' ')
toBeSorted = []
for i in arr:
    toBeSorted.append(int(i))
    

totalNumberOfSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n - 1):
        
        if toBeSorted[j] > toBeSorted[j+1]:
            temp = toBeSorted[j]
            toBeSorted[j] = toBeSorted[j+1]
            toBeSorted[j+1] = temp
            numberOfSwaps += 1
    totalNumberOfSwaps += numberOfSwaps

    if numberOfSwaps == 0:
        break
            
print('Array is sorted in {} swaps.'.format(totalNumberOfSwaps))
print('First Element: {}'.format(toBeSorted[0]))
print('Last Element: {}'.format(toBeSorted[-1]))