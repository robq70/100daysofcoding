def pattern_4(rows):
    k = rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k += 1
        for j in range(0, i + 1):
            print("*", end=" ")
            print("\r")
        k = 2 * rows - 2
        for i in range(0, rows + 1):
            for j in range(0, k):
                print(end=" ")
            k -= 1
            for j in range(0, i + 1):
                print("*", end=" ")
            print("\r")


n = 5

pattern_4(n)
