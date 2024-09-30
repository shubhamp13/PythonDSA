import  array as p
nums=p.array('i',[8,7,9,3,5])

#adding element to an array
nums.append(6)
print(nums)

#adding multiple elements to an array
nums2=p.array('i',[9,6,3,1])
nums.extend(nums2)
print(nums)

#updating elements
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[5])
print(nums[6])
print(nums[7])
print(nums[8])
print(nums[9])

nums[0]=1
print(nums)

#for updating multiple elements
nums[1:6]=p.array('i',[2,5,8,0,2])
print(nums)
#1,2,5,8,0,2,9,6,3,1
