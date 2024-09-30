#list
#1.list are ordered collection of elements
#2.list is mutable (we can update list)
#3.duplicates are allowed in the list


#1.Ordered

l1=[1,8,0,3,1,9,9,8]
print(f"In which we have inserted {l1}")


#2.Mutable

print(f"l1[0] = {l1[0]} ")
#now we can update it also
l1[0]=9
print(f"l1[0] = {l1[0]} ")
print(l1)

#3.duplicates are also allowed
print(l1.count(9))

