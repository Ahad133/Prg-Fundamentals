s=eval(input("enter stopping value"))

for row in range(1,s):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")