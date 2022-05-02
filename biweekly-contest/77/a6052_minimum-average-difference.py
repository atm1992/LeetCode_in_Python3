# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [nums[0]]
        for i in range(1, n):
            pre_sum.append(pre_sum[i - 1] + nums[i])
        diff = float('inf')
        res = 0
        for i in range(n):
            num1 = 0 if i == n - 1 else (pre_sum[n - 1] - pre_sum[i]) // (n - 1 - i)
            num2 = pre_sum[i] // (i + 1)
            tmp = abs(num1 - num2)
            if tmp < diff:
                diff = tmp
                res = i
            if tmp == 0:
                break
        return res


if __name__ == '__main__':
    print(Solution().minimumAverageDifference(nums=[0]))
