rows = 5
columns = 5

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if j == columns:
            print(i + 1, end="")
        else:
            print(i, end="")
    print()
