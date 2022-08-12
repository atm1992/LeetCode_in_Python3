# -*- coding: UTF-8 -*-
"""
title: 必须拿起的最小连续卡牌数
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.
Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.


Example 1:
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:
Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.


Constraints:
1 <= cards.length <= 10^5
0 <= cards[i] <= 10^6
"""
from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # 记录每个num最后出现的index
        num2idx = defaultdict(int)
        n = len(cards)
        res = n + 1
        for idx, num in enumerate(cards):
            if num in num2idx:
                tmp = idx - num2idx[num] + 1
                if tmp < res:
                    res = tmp
                if tmp == 2:
                    break
            num2idx[num] = idx
        return -1 if res == n + 1 else res


if __name__ == '__main__':
    print(Solution().minimumCardPickup(cards=[3, 4, 2, 3, 4, 7]))
