#set
#1.In set order is not maintained (unordered)
#2.duplicates are not allowed
#3.set are immutable we can not change, but we can add and remove

#set is unordered collection of unique elements which are immutable
# set is immutable in nature
#duplicate elements are not allowed in set

#1.Order is not maintained
unique_elements={8,7,9,3,5,6,9,6,3,1}
print(unique_elements)

#2.duplicate elements are not allowed
unique_elements2={1,1,1,1,2,2,2,2,3,3,3,3}
print(unique_elements2)

#3.immutable we can not change element but we can add or remove

immutable_nature={1,8,0,3,1,9,9,8}
# immutable_nature[0]=10  # We can not perform assignment operation
print(immutable_nature)
immutable_nature.add(10)
print(immutable_nature)
immutable_nature.remove(10)
print(immutable_nature)



