#countdown timer
import time

timer=int(input("Enter timer"))

for x in reversed(range(0, timer)):
    print(x)
    time.sleep(1)
print("Done")


#for reversing

for x in range(timer,0,-1):
    print(x)