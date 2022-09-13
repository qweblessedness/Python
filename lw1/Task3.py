N=int(input("Enter N: "))
while(N<1 or N>9):
  N=int(input("Enter N again: "))
for row in range(1, N+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
