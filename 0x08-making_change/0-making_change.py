#!/usr/bin/python3
""" fewest number of coins needed """


def makeChange(coins:list, total:int) -> int:
    """ fewest number of coins needed

    Args:
        coins (List): list of the values of the coins
        total (int): the total amount

    Returns:
        int: return the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        count = total // coin
        coin_count += count
        total -= count * coin

    if total == 0:
        return coin_count
    else:
        return -1
