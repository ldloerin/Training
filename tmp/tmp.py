lList = ['A','a',5,3,8,1,9,6,3,5,3,'a','A']

for i in range(0, len(lList)):
    if type(lList[i]) == int:
        lList[i] = str(lList[i])
    
print(lList)
lList.sort()
print(lList)
lList.reverse()
print(lList)