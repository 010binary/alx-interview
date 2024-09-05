#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
    x (int): Number of rounds.
    nums (list of int): Array of n for each round.

    Returns:
    str: Name of the player that won the most rounds, or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    # Count the number of primes up to each number n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
