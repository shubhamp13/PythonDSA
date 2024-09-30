#list methods
from itertools import count

phone_no=[8,7,9,3,5,6,9,6,3,1]
print(phone_no)

#1.append()====>It will add element at the end of the list
phone_no.append(0)
print(phone_no)

#2.extend([])====>it will append another list
phone_no2=[9,5,7,9,6,7,8,3,7,5]
phone_no.extend(phone_no2)
print(phone_no)

#3.insert(position,element)===>It will insert element at specific position
phone_no.insert(0,18)
print(phone_no)

#4.remove(element)===>it will remove the given element from list first occurrence only
phone_no.remove(9)
print(phone_no)

#5.pop()===>It will remove the last element of list
last_element=phone_no.pop()
print(last_element)
print(phone_no)

#6.clear()====>It will remove all element of list
print(f"before calling clear {phone_no2}")
phone_no2.clear()
print(f"after calling clear {phone_no2}")

#7.count(object)====>It will count the occurrence of given element   in the list
print(f"count of 7 is {phone_no.count(7)}")

#8.index(element)====>It will return  index of given element
print(phone_no.index(5))

#9.sort()====>it will sort the list
phone_no.sort()
print(phone_no)

#10.reverse()====>It will reverse the list
phone_no.reverse()
print(phone_no)

#11.copy()====>copy
new_list=phone_no.copy()
print(new_list)

#1.append()====>It will add element at the end of the list
#2.extend([])====>it will append another list
#3.insert(position,element)===>It will insert element at specific position
#4.remove(element)===>it will remove the given element from list first occurrence only
#5.pop()=====>It will remove the last element of list
#6.clear()====>It will remove all element of list
#7.count(object)====>It will count the occurrence of given element   in the list
#8.index(element)====>It will return  index of given element
#9.sort()====>it will sort the list
#10.reverse()====>It will reverse the list

