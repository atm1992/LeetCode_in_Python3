# -*- coding: UTF-8 -*-
"""
title: 最大数
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.


Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
"""
import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """排序。自定义比较函数"""

        def compare(a: str, b: str) -> int:
            # 对于输入a,b来说，若要A排在B的前面，则返回负数；若要B排在A的前面，则返回正数；返回0表示按原始顺序。
            # 希望最终是降序排列，大在左，小在右。若 int(b + a) - int(a + b) 返回正数，则表示B排在A的前面
            return int(b + a) - int(a + b)

        res = sorted(map(str, nums), key=functools.cmp_to_key(compare))
        # nums = [0, 0]
        return '0' if res[0] == '0' else ''.join(res)


if __name__ == '__main__':
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
