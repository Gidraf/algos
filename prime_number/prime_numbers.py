prime_numbers = []
max_val = 100
for i in range(max_val):
    is_prime = True
    if i == 0:
        is_prime = False
    for k in range(1,i):
        if k > 1 and i != k and i % k == 0:
            is_prime = False
    if is_prime:
       prime_numbers.append(i)
print(prime_numbers)
