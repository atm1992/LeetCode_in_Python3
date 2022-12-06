# -*- coding: UTF-8 -*-
"""
title: 旋转数字
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. For example:
    0, 1, and 8 rotate to themselves,
    2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
    6 and 9 rotate to each other, and
    the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].


Example 1:
Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Example 2:
Input: n = 1
Output: 0

Example 3:
Input: n = 2
Output: 1


Constraints:
1 <= n <= 10^4
"""
from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        """暴力枚举"""
        res = 0
        invalid_digits, good_digits = {'3', '4', '7'}, {'2', '5', '6', '9'}
        for num in range(1, n + 1):
            digits = set(str(num))
            if not digits.intersection(invalid_digits) and digits.intersection(good_digits):
                res += 1
        return res

    def rotatedDigits_2(self, n: int) -> int:
        """
        数位 DP
        因为在一个数的前面添加前导零，并不会改变该数的好坏，所以可将n以内的所有数字的长度都认为是len(str(n))，长度不足的，前补0。
        f(idx, is_bound, is_good) 表示满足以下要求的好数的个数：
        1、idx的取值范围：[0, len(str(n)) - 1]，最高位的下标为0，从最高位向最低位逐位转移
        2、is_bound 表示之前的idx位是否达到了上限，即 是否等于str(n)[:idx]，若达到了上限，则表示当前idx位最多只能取到str(n)[idx]，而不能再直接取到9了
        3、is_good 表示当前遍历的该数字，其前idx位中是否存在{2, 5, 6, 9}，若存在，则表示该数字是一个好数；若不存在，则表示暂时还不是好数。
        """
        digits = str(n)
        size = len(digits)
        invalid_digits, good_digits = {3, 4, 7}, {2, 5, 6, 9}

        @lru_cache(maxsize=None)
        def dfs(idx: int, is_bound: bool, is_good: bool) -> int:
            if idx == size:
                # 若is_good为True，则表示当前遍历的这个数字是一个好数，因此res会加1，否则加0。所有不含{3, 4, 7}的数字，最终都会走到这里
                return int(is_good)
            res = 0
            up_bound = int(digits[idx]) if is_bound else 9
            for d in range(up_bound + 1):
                if d not in invalid_digits:
                    # 只有当is_bound为True，并且当前数位d也等于up_bound时，is_bound才会继续为True，相当于在贴着str(n)的上限走
                    # 只要有一个数位在{2, 5, 6, 9}以内，这个数字就会一直是好数。当然，前提是该数字不含{3, 4, 7}
                    res += dfs(idx + 1, is_bound and d == up_bound, is_good or d in good_digits)
            return res

        return dfs(0, True, False)


if __name__ == '__main__':
    print(Solution().rotatedDigits_2(10))
