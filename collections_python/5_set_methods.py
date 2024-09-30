numbers={1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9}
print(numbers)

#1.add(object)==>It will add object at last
numbers.add(10)
print(numbers)

#2.update()===>we can pass set,list ,tuple to add elements in set
numbers.update([11,12,13])
print(numbers)

#3.remove(element)====>It will remove the specified element from set
numbers.remove(12)
print(numbers)
# numbers.remove(100)#It will give keyError

#4.discard(element)===>It will remove specified element from set and it will not raise error if element is not present
numbers.discard(100)
print(numbers)

#5.pop()=====>It removes random element in case of set
my_set={1,8,3,1,9,9,8}
last_element=my_set.pop()
print(last_element)

#6.clear()===>it will remove all elements of set
my_set.clear()
print(my_set)

#7.union()===>it will combine two sets and form new set
set1={1,2,3}
set2={4,5,6}
set3=set1.union(set2)
print(set3)

#8.intersection()====>it will create a set with common elements of two set
set1={1,2,3}
set2={2,3,4,5}
set3=set1.intersection(set2)
print(set3)

#9 difference()==>it will returns the different element form two set
et1={1,2,3}
set2={2,3,4,5}
set3=set1.difference(set2)
set4=set2.difference(set1)
print(set3)
print(set4)

#10.symmetric_difference():=It will include elements which are not in both sets
et1={1,2,3}
set2={2,3,4,5}
set3=set1.symmetric_difference(set2)
print(set3)

#11.isSubset()====>It will return true if given set is present in another set
set1={1,2,3}
set2={1,2,3,4,5,6}
print(set1.issubset(set2))

#12.superset()====>It will check every element present in both set returns true else false
set1={1,2,3}
set2={1,2,3,4}
print(set1.issuperset(set2))

#13.isdisjoint(): Returns True if the set has no elements in common with another set
set1={1,2,3}
set2={4,5,6}
print(set1.isdisjoint(set2))



#1.add(object)==>It will add object at last
#2.update()===>we can pass set,list ,tuple to add elements in set
#3.remove(element)====>It will remove the specified element from set
#4.discard(element)===>It will remove specified element from set and it will not raise error if element is not present
#5.pop()=====>It removes random element in case of set
#6.clear()===>it will remove all elements of set
#7.union()===>it will combine two sets and form new set
#8.intersection()====>it will create a set with common elements of two set
#9 difference()==>it will returns the different element form two set
#10.symmetric_difference():=It will include elements which are not in both sets
#11.isSubset()====>It will return true if given set is present in another set
#12.superset()====>It will check every element present in both set returns true else false
#13.isdisjoint(): Returns True if the set has no elements in common with another set





