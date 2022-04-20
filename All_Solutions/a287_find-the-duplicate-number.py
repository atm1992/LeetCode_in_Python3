# -*- coding: UTF-8 -*-
"""
title: 寻找重复数
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.


Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3


Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        二分查找。假设重复的那个数字为target，cnt[i] 表示小于等于i的数字的出现次数，若i<target，则cnt[i]<=i；若i>=target，则cnt[i] > i。因为总共是n+1个数，而不是n个数。
        所以可使用二分来查找第一个满足cnt[i] > i 的数，那个数就是target。
        那个重复的数字会出现两次或多次，不一定只是两次。而且nums不一定是完整的序列1~n，中间可能会缺失某些数。所以不能用 sum(nums) - sum(range(len(nums)))
        """
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left

    def findDuplicate_2(self, nums: List[int]) -> int:
        """
        快慢指针。类似于查找链表中的环入口点。快慢指针都从index 0开始走，下一步到达的index为nums[0]。
        0 ——> i (nums[0])  ——> j (nums[i]) ——> k (nums[j]) ——> ……
        假设nums = [3, 4, 1, 4, 2, 4]，nums总共有n+1 == 6个元素，元素值均在范围 [1, 5] 内。
        slow指针：0 ——> 3 (nums[0])  ——> 4 (nums[3]) ——> 2 (nums[4]) ——> 1 (nums[2]) ——> 4 (nums[1]) ——> 2 (nums[4]) ——> ……
        由上可知，虽然nums中有3个4，但其实只会用到下标为3、1的4，并不会走到下标为5的4。nums[3] 进入环，nums[1] 回到环
        所以即使元素的重复次数大于2，该重复元素的入度始终为2，非重复元素的入度始终为1。
        """
        # nums的最小值为1，所以nums中没有哪个元素会指向下标0(元素值等于0)，因此，下标0没有前置节点
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # slow, fast 都变成一步步走
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast


if __name__ == '__main__':
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))
