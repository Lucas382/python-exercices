

def FF(y):
    ++n
    if y < 2:
        return 1
    else:
        return y * FF(y-1)


x = 5
n = 0
w = FF(x)
w = w-50

print(w,n)