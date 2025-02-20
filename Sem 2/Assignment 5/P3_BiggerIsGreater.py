t = int(input("Enter the number of test cases: "))
res = []

for _ in range(t):
    w = list(input("Enter the word: "))
    n = len(w)
    i = n - 2

    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        res.append("no answer")
    else:
        j = n - 1

        while w[j] <= w[i]:
            j -= 1
        w[i], w[j] = w[j], w[i]
        w = w[:i + 1] + w[i + 1:][::-1]

        res.append("".join(w))

print("\n".join(res))
