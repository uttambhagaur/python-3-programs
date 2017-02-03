#for and while loops
lists = [1,2,4,5,"uttam","singh"]
names = ["uttam","singh","bhagaur"]
for list in lists:
    print(list)

i=len(lists)-1
while(i>=0):
    print(lists[i])
    i=i-1
for i,j in zip(lists,names):
    print(i,j)
