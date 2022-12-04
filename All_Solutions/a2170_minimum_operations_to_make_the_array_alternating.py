# -*- coding: UTF-8 -*-
"""
title: 使数组变成交替数组的最少操作数
You are given a 0-indexed array nums consisting of n positive integers.
The array nums is called alternating if:
    nums[i - 2] == nums[i], where 2 <= i <= n - 1.
    nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.
Return the minimum number of operations required to make the array alternating.


Example 1:
Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations.

Example 2:
Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
from collections import defaultdict
from typing import List, Tuple


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        贪心 + 分类讨论
        分别统计奇数下标出现最多次的元素和偶数下标出现最多次的元素。为避免这两个元素相等，因此还需再统计奇数下标出现次数第二多的元素和偶数下标出现次数第二多的元素
        """
        def get_1_2(num2cnt: dict) -> Tuple[int, int, int, int]:
            # 因为1 <= nums.length，所以当nums.length为1时，even2cnt为空
            if not num2cnt:
                # 1 <= nums[i]
                return 0, 0, 0, 0
            else:
                tmp = sorted(num2cnt.items(), key=lambda item: -item[1])
                if len(tmp) == 1:
                    return tmp[0][0], tmp[0][1], 0, 0
                else:
                    return tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1]

        n = len(nums)
        odd2cnt, even2cnt = defaultdict(int), defaultdict(int)
        for i, num in enumerate(nums):
            if i & 1:
                odd2cnt[num] += 1
            else:
                even2cnt[num] += 1

        odd_1_num, odd_1_cnt, odd_2_num, odd_2_cnt = get_1_2(odd2cnt)
        even_1_num, even_1_cnt, even_2_num, even_2_cnt = get_1_2(even2cnt)
        if odd_1_num != even_1_num:
            return n - (odd_1_cnt + even_1_cnt)
        return n - max(odd_1_cnt + even_2_cnt, odd_2_cnt + even_1_cnt)


if __name__ == '__main__':
    print(Solution().minimumOperations(nums=[1, 2, 2, 2, 2]))
