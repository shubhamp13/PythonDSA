#for loop It will execute block of code for fixed number of times


for x in range(1,11):
    print(x)

# for iterating in reverse order
for x in reversed(range(10,21)):
    print(x)

# it will step by 2
for x in range(1,11,2):
    print(x)

#String
name="Shubham Pandit Puri"
for x in name:
    print(x)

#continue
for x in range (1,23):
    if x==10:
        continue
    else:
        print(x)

#break
for x in range(1,10):
    if x==6:
        break
    print(x)