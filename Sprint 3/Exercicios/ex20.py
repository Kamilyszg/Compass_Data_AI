a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

a_reversa = []

for i in range(len(a) - 1, -1, -1):
    a_reversa.append(a[i])

print(a_reversa)