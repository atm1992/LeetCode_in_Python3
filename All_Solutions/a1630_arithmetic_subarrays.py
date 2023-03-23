# -*- coding: UTF-8 -*-
"""
title: 等差子数组
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
For example, these are arithmetic sequences:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
The following sequence is not arithmetic:
    1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.
Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.


Example 1:
Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.

Example 2:
Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]


Constraints:
n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        模拟 + 数学
        判断一个子数组是否为等差数列，公差d = (max(nums) - min(nums)) / (len(nums) - 1)
        等差数列中的每个元素 (num - min(nums)) / d 的计算结果应依次满足 [0, len(nums) - 1]，这里可使用哈希表来判断
        """

        def check(l: int, r: int) -> bool:
            # 若只有两个元素，则一定是等差数列
            if l + 1 == r:
                return True
            max_num, min_num = -10 ** 5, 10 ** 5
            for i in range(l, r + 1):
                max_num = max(max_num, nums[i])
                min_num = min(min_num, nums[i])
            # 说明数列中的所有元素都相等，因此是一个公差为0的等差数列
            if max_num == min_num:
                return True
            if (max_num - min_num) % (r - l) != 0:
                return False
            d = (max_num - min_num) // (r - l)
            visited = set()
            for i in range(l, r + 1):
                if (nums[i] - min_num) % d != 0 or (nums[i] - min_num) // d in visited:
                    return False
                visited.add((nums[i] - min_num) // d)
            return True

        return [check(i, j) for i, j in zip(l, r)]


if __name__ == '__main__':
    print(Solution().checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                              l=[0, 1, 6, 4, 8, 7], r=[4, 4, 9, 7, 9, 10]))
