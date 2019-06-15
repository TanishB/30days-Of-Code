# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())
stringList = []
for i in range(test):
    string = input()
    stringList.append(string)
for s in stringList:
    i = 0
    even = ''
    odd = ''
    for i in range(len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even , odd)
