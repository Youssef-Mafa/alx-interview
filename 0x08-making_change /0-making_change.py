#!/usr/bin/python3
"""
Combined and optimized makeChange implementation
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list): The denominations of coins available.
        total (int): The target total to achieve using the coins.
    
    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if it is not possible to achieve the total.
    """
    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1

    coins.sort(reverse=True)  # Use larger denominations first
    change = 0

    for coin in coins:
        if total == 0:
            break
        # Calculate the maximum number of this coin we can use
        count = total // coin
        change += count
        total -= count * coin

    return change if total == 0 else -1
