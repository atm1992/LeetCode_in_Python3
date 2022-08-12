# -*- coding: UTF-8 -*-
"""
title: 缺失的区间
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b


Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"

Example 2:
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.


Constraints:
-10^9 <= lower <= upper <= 10^9
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.
"""
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [f'{lower}->{upper}']
        res = []
        if lower != nums[0]:
            if nums[0] - 1 > lower:
                res.append(f'{lower}->{nums[0] - 1}')
            else:
                res.append(str(lower))
        n = len(nums)
        idx = 0
        while True:
            while idx < n - 1 and nums[idx] + 1 == nums[idx + 1]:
                idx += 1
            if idx < n - 1:
                tmp = str(nums[idx] + 1)
                if nums[idx + 1] - 1 > nums[idx] + 1:
                    tmp += f'->{nums[idx + 1] - 1}'
                res.append(tmp)
                idx += 1
            else:
                if nums[-1] != upper:
                    if nums[-1] + 1 < upper:
                        res.append(f'{nums[-1] + 1}->{upper}')
                    else:
                        res.append(str(upper))
                break
        return res

    def findMissingRanges_2(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """类似双指针的思路"""
        res = []
        pre = lower - 1
        # 添加终止边界，不修改原始数组
        new_nums = nums + [upper + 1]
        for num in new_nums:
            if num - 1 > pre + 1:
                res.append(f'{pre + 1}->{num - 1}')
            elif num - 1 == pre + 1:
                res.append(str(pre + 1))
            pre = num
        return res


if __name__ == '__main__':
    print(Solution().findMissingRanges(nums=[-1], lower=-1, upper=-1))
