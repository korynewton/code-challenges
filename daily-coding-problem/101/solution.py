import math

#brute force n/2 time complexity
def return_primes_summed_to_n(n):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3,int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True

    for i in range(2,int(n/2)+1):
        i_pair = n - i
        
        if is_prime(i_pair) and is_prime(i):
          return [i,i_pair]


