def readint():
    return int(input())

    n = readint()
    k = readint()

    grades = sorted((readint() for i in range(n)), reverse=True)

    while (k < n) and (grades[k] == grades[k - 1]):
        k += 1

    print(k)