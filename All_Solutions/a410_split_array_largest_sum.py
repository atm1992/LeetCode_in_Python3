# -*- coding: UTF-8 -*-
"""
title: 分割数组的最大值
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.


Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4


Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """二分猜答案(二分查找 + 贪心)"""

        def check(sub_sum: int) -> bool:
            """验证是否存在分割子数组的最大和不超过sub_sum的分隔方案。若最终的子数组个数小于等于m，则说明方案可行，可以继续减小sub_sum"""
            cnt = tmp_sum = 0
            for num in nums:
                # 保证每个tmp_sum都小于等于sub_sum
                if tmp_sum + num > sub_sum:
                    cnt += 1
                    # 若当前已切分出m个子数组，则最终的子数组个数一定大于m，因为当前的 tmp_sum = num > 0
                    if cnt == m:
                        return False
                    # 只有当num大于0时，才可能会切分出一个新的子数组。若num为0，则会直接将其划分到上一个子数组
                    tmp_sum = num
                else:
                    tmp_sum += num
            return True

        total = sum(nums)
        if m == 1:
            return total
        left, right = max(max(nums), total // m), total
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                # 说明方案可行，可以继续减小
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().splitArray(nums=[7, 2, 5, 10, 8], m=2))
