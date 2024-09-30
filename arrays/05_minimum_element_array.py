import array as p
nums=p.array('i',[8,7,9,3,5,6,9,6,3,1])
smallest=nums[0]

for x in nums:
    if(x<smallest):
        smallest=x
print(smallest)