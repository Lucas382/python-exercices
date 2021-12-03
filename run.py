v = [2, 0, 4, 3, 1]

for i in range(len(v)):
    for j in range(len(v)-i-1):
        if i == 0 and j == 1 or i == 1 and j == 0 or i == 1 and j == 2:
            print("i vale: ", i, "")
            print("j vale: ", j, "")
            print(v)
            print()
        if v[j] > v[j+1]:
            a = v[j]
            v[j] = v[j+1]
            v[j+1] = a
print(v)
