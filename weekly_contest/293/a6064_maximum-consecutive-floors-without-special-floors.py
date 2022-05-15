# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        res = 0
        nums = special + [bottom - 1, top + 1]
        nums.sort()
        for i in range(1, len(nums)):
            tmp = nums[i] - nums[i - 1] - 1
            res = max(res, tmp)
        return res


if __name__ == '__main__':
    print(Solution().maxConsecutive(bottom=6, top=8, special=[7, 6, 8]))
