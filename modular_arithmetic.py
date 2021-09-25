import random
import time
import numpy as np

def load_small_primes():
    pfile =  open("1000primes.txt", "r")
    small_primes = [int(num) for num in pfile.read().split(',')]
    return small_primes

small_odd_primes = load_small_primes()
print("Small odd primes loaded : {}...".format(small_odd_primes[:5]))


def probable_prime(size):
    assert size > 0
    times = []
    s = size-1
    smallest = 1<<s
    largest = (1<<(s+1))-1
    while True:
        n = random.randint(smallest,largest)
        if even(n) or divisible_by_small_prime(n):
            continue
        a = random.randint(2,n-1)
        start = time.perf_counter()
        # mod_computation = pow_n_mod_n(a,n) OLD
        mod_computation = modular_exponentiation(a,n)
        stop = time.perf_counter()
        times.append(stop-start)

        if mod_computation == 1:
            return n, times
        # print("odd -not prime")

def even(n):
    return (n&1) != 1

def pow_n_mod_n(a,n):
    return modulo ((a**(n-1)), n)

def modular_exponentiation(a,n):
    # Returns the value a**(n-1) mod n
    return pow(a,(n-1),n)

def divisible_by_small_prime(n, resolution=1000):
    global small_odd_primes
    for small_prime in small_odd_primes[:resolution]:
        if n == small_prime:
            # In this case n is a prime number, and we return
            # False to indicate it is not divisible by any of
            # the smaller primes
            return False
        if modulo(n, small_prime) == 0:
            # print("diviseble by small prime")
            return True
    return False

def modulo(a,b):
    """returns a mod b"""
    return a % b

def seconds_to_prefix(sec):
    if sec < 1:
        ms = sec * 1000
        return "{} ms".format(round(ms,4))
    elif sec < 60:
        return "{} s".format(round(sec,4))
    else:
        min = int(sec) // 60
        rem = seconds_to_prefix(sec-60*min)
        return "{} min and {}".format(min,rem)

def main():
    mod_dict ={}
    for s in range(3072,3073):
        print("finding prime of size {} bits...".format(s))
        tstart = time.perf_counter()
        p, lp = probable_prime(s)
        tend = time.perf_counter()
        total_time = tend-tstart
        mod_dict[s] = (p,lp, total_time)
        print("\tFound: ",p)
    
    for key,val in mod_dict.items():
        t = seconds_to_prefix(np.mean(val[1]))
        totalt = seconds_to_prefix(val[2])
        print("size {}: \n\tProbable prime: {} \
            \n\tAverage mod cmp time: {} \
            \n\tNumber of mod cmps: {} \
            \n\tTotal time: {}".format(key, val[0], t, len(val[1]), totalt))
    
if __name__ == "__main__":
    main()
    # p = probable_prime(8)
    # print(seconds_to_prefix(16767.4))
    # print(seconds_to_prefix(7.4))
    # print(seconds_to_prefix(.456))

