def primes():
    item = 1
    while True:
        item += 1
        is_prime = True
        for i in range(2, item):
            if item % i == 0:
                is_prime = False
                break
        if is_prime:
            yield item
