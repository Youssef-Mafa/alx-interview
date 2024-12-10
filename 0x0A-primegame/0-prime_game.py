#!/usr/bin/python3
"""
Prime Game Module

A game where Maria and Ben take turns choosing prime numbers and removing their multiples.
The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    
    Args:
        x (int): Number of rounds
        nums (list): Array of n numbers representing the upper limit for each round
    
    Returns:
        str: Name of the winner ("Maria" or "Ben") or None if it's a tie or invalid input
    """
    if not nums or x <= 0 or x != len(nums):
        return None

    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    maria_wins = ben_wins = 0

    for n in nums:
        prime_count = sum(sieve[2:n + 1])

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
