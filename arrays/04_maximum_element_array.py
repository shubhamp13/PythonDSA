import array as p
mobile_no=p.array('i',[8,7,9,3,5,6,9,6,3,1])
largest=mobile_no[0]

for num in mobile_no:
    if num > largest:
        largest=num
print(f'Largest Element in Array Is {largest}')