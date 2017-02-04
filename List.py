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

#List Methods

#Here are some other common list methods.

#list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
#list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
#list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
#list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
#list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
#list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
#list.reverse() -- reverses the list in place (does not return it)
#list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
