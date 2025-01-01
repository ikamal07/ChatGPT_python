def find_max(x,y,z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(find_max(8,7,7))

