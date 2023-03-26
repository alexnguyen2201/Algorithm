def closest_prime(n):
    if n <= 1:  # handle 0 & 1 as special cases
        return 2

    sieve_limit = 2 * n

    sieve = [False, False] + [True] * (sieve_limit - 2)

    prime_candidate = number = 2

    while number < sieve_limit:
        if sieve[number]:
            if number == n:
                return n  # n is prime

            if number > n:
                if (number - n) < (n - prime_candidate):
                    return number

                return prime_candidate

            prime_candidate = number

            sieve_limit = 2 * n - prime_candidate  # reduce sieve size

            for index in range(number * number, sieve_limit, number):
                sieve[index] = False

        number += 1

    return prime_candidate  # ran off end of sieve


if __name__ == "__main__":
    print(1000, closest_prime(1000))
    print(500, closest_prime(500))
