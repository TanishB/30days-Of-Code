a = []
actualReturn = input().split(' ')
for i in actualReturn:
    a.append(int(i))

e = []
expectedReturn = input().split(' ')
for i in expectedReturn:
    e.append(int(i))
#print(a,e)
# If Else ladder Starts
fine = 0

if a[2] < e[2]:
    
    fine = 0
elif a[2] == e[2]:
    #Check month
    
    if a[1] < e[1]:
        
        fine = 0
    elif a[1] == e[1]:
        #Check day
        
        if a[0]<=e[0]:
            fine = 0
            
        else:
            
            fine = (a[0] - e[0]) * 15
            
    else:
        fine = fine = (a[1] - e[1]) * 500
else:
    fine = 10000

print(fine)