# -*- coding: UTF-8 -*-
"""
title: 装满杯子需要的最短总时长
You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.
You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.


Example 1:
Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.

Example 2:
Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.

Example 3:
Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.


Constraints:
amount.length == 3
0 <= amount[i] <= 100
"""
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """贪心"""
        amount.sort()
        a, b, c = amount
        if c >= a + b:
            return c
        # c < a + b，每次都让c与a/b中的一个各减1，当c减到0时，b >= a >= 0
        for _ in range(c):
            # 始终保持 a <= b
            if a < b:
                b -= 1
            else:
                a -= 1
        # 最后剩下的a、b，一定是a先消耗完，然后b再慢慢减1。所以减完c次后，还需再减剩余的b次
        return c + b


if __name__ == '__main__':
    print(Solution().fillCups(amount=[5, 4, 4]))
