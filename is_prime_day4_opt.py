def is_prime(x):
    if x <= 1:
        return False  # Not prime
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
        
    return True
        
print(is_prime(7))
print(is_prime(27))
print(is_prime(37))


