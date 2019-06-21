num = int(input())
for i in range(num):
    t = []
    temp = input().split(' ')
    n = int(temp[0])
    k = int(temp[1])
    print(k-1 if ((k-1) | k) <= n else k-2)

    
