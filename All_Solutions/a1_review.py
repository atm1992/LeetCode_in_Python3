# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """哈希表"""
        num2idx = {}
        for idx, num in enumerate(nums):
            if target - num in num2idx:
                return [num2idx[target - num], idx]
            num2idx[num] = idx


if __name__ == '__main__':
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
