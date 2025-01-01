def is_prime(x):
    flag = 0
    if x == 2:
        flag = 1
    
    for i in range(2,x):
        y=x%i
        if y == 0:
            flag = 1

    if flag == 0:
        print("Not Prime")
    else:
        print("prime")

is_prime(2)
        