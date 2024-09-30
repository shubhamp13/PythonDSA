#nested loop: loop inside another loop
rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))

for x in range(rows+1):
    for y in range(1,columns+1):
        print('*',end=" ")
    print()