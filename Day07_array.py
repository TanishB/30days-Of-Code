n = int(input())
array = []
elements = input().split(' ')
for element in elements:
    array.append(int(element))
i = n - 1
while i>=0:
    print(array[i],end = ' ')
    i -= 1
