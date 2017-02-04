list = [21,12,14,15,16,20]
#listNew = list
#list can not be copy into listNew it just point out copy will done with
#listNew = list[:]
print(type(list))
print(list[ :5])
print(list[2:])
print(list+[1,3,4,9])
print(list[:])
list[2]=120
print(list[:])
l=len(list)
print(l)
del list[5]
list.append("add")
print(list[:])
#add to specific index
list.insert(2,"position")
print(list[:])
#remove by content
list.remove("position")
print(list[:])
#It is used to show all function of list
dir(list)
help(list.pop)#show how to use method/function
