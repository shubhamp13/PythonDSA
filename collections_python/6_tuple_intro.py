#tuple
#1.elements in the tuple are ordered
#2.tuple is immutable in nature we can not even add and remove
#3.duplicates are allowed
#4.tuple operations are faster
#tuple is ordered collection of fixed elements

# tuple is ordered
t=(1,2,3)
print(t)

# tuple is completely immutable we can not even add or remove element
print(t[0])
# t[0]=10
print(t)

#operation on tuple

#1.concatenation operation
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)

# * operator==>It will repeat the tuple elements given times
t3=t1*2
print(t3)

#methods
#1.count()===>It will count the occurrence of given element in tuple

t1=(1,2,3,1,1,1,2,3)
print(t1.count(1))

#2 index(): Returns the index of the first occurrence of a specified value.
print(t1.index(3))
