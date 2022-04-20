# -*- coding: UTF-8 -*-
"""
title: Nim 游戏（取物游戏）
You are playing the following Nim Game with your friend:
    Initially, there is a heap of stones on the table.
    You and your friend will alternate taking turns, and you go first.
    On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
    The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.


Example 1:
Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.

Example 2:
Input: n = 1
Output: true

Example 3:
Input: n = 2
Output: true


Constraints:
1 <= n <= 2^31 - 1
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        数学推理。自己取完后，堆中最后剩余的石头数为4时，对方必输。由于是自己先取，只要在自己取完第一次后，剩余的石头总数为4的倍数，
        就一定能赢对方，因为之后无论对方取多少个，自己都取 4 - 对方取的个数，始终让剩余的石头总数维持4的倍数。
        因此，只要石头总数n不是4的倍数，自己就一定能赢。
        """
        return n % 4 != 0


if __name__ == '__main__':
    print(Solution().canWinNim(4))
