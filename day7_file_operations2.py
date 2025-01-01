with open("squares.txt", "w") as f1:
    for i in range(1,11):
        k=i**2
        f1.write(str(k))
        f1.write("\n")