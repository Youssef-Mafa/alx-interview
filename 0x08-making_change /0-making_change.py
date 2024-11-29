#!/usr/bin/python3
"""Optimized Making Change Algorithm"""
def makeChange(coins, total):
    """
    Calculate fewest number of coins needed to meet total
    Args:
        coins: list of coin values
        total: target sum
    Returns:
        Number of coins needed, -1 if impossible, 0 if total <= 0
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
        
    coins.sort(reverse=True)
    change = 0
    
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
            
    return -1
