#!/usr/bin/python3
""" fewest number of coins needed """


def makeChange(coins, total):
    """


    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        count = total // coin  # Max number of this coin we can use
        coin_count += count
        total -= count * coin

    if total == 0:
        return coin_count
    else:
        return -1
