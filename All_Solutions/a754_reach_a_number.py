# -*- coding: UTF-8 -*-
"""
title: 到达终点数字
You are standing at position 0 on an infinite number line. There is a destination at position target.
You can make some number of moves numMoves so that:
    On each move, you can either go left or right.
    During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.


Example 1:
Input: target = 2
Output: 3
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to -1 (2 steps).
On the 3rd move, we step from -1 to 2 (3 steps).

Example 2:
Input: target = 3
Output: 2
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to 3 (2 steps).


Constraints:
-10^9 <= target <= 10^9
target != 0
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        """
        分类讨论 + 数学
        若target为负数，则可根据对称性，将问题转换成target为正数。因此，只需考虑target为正数的情况。
        1、若一直朝着target方向走n步，恰好能走到target，即 sum(n) = n*(n+1)/2 == target，则最终结果就是n；
        2、若 sum(n) > target
            2.1、若 delta =  sum(n) - target 为偶数，则可从之前的n步中选出若干步的方向为反方向，这些步数之和为 delta / 2，此时的最终结果也是n；
            2.2、若 delta 为奇数，则此时的delta / 2不是整数，因此不可能是若干步数之和，所以为了使得delta为偶数，需要再走1 ~ 2步
                2.2.1、若n+1为奇数，则delta' = (n+1) + delta，此时的delta'变成了偶数，从这n+1步中选出若干步的方向为反方向，这些步数之和为 delta' / 2，此时的最终结果为n+1；
                2.2.2、若n+1为偶数，则(n+1) + delta依旧为奇数，因此还需再走一步，即 delta' = (n+2) + (n+1) + delta，此时的最终结果为n+2。

        为什么一定存在若干步数之和等于 delta / 2 ？已知 delta / 2 < sum(n)，下面使用数学归纳法证明 [1, sum(n)] 中的任意整数均可由[1, n]中的若干个数组合出。
        当n=1时，sum(1) = 1，[1, 1]中的若干个数可以组合出[1, sum(1)]中的任意整数；
        当n=2时，sum(2) = 3，[1, 2]中的若干个数可以组合出[1, sum(2)]中的任意整数；
        ……
        假设当n=k时，[1, k]中的若干个数可以组合出[1, sum(k)]中的任意整数；
        则当n=k+1时，[1, sum(k)] + (k+1) ==> [k+2, sum(k) + (k+1)] ==> [k+2, sum(k+1)]，
            易知，当k>2时，k+2 < sum(k)，所以根据数学归纳法，可知[1, k+1]中的若干个数可以组合出[1, sum(k+1)]中的任意整数。
        """
        target = abs(target)
        sum_n = n = 1
        while sum_n < target or (sum_n - target) & 1:
            n += 1
            sum_n += n
        return n


if __name__ == '__main__':
    print(Solution().reachNumber(4))
