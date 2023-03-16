# -*- coding: UTF-8 -*-
"""
title: 通过最少操作次数使数组的和相等
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.
In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.
Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.


Example 1:
Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].

Example 2:
Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.

Example 3:
Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].


Constraints:
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[i] <= 6
"""
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """贪心 + 哈希表"""
        # 其余情况下，一定可以使diff减至0
        if len(nums1) > 6 * len(nums2) or len(nums2) > 6 * len(nums1):
            return -1
        diff = sum(nums1) - sum(nums2)
        if diff == 0:
            return 0
        # 保证 sum(nums1) > sum(nums2)，然后通过减小nums1中的元素以及增大nums2中的元素来将diff减至0
        if diff < 0:
            diff = -diff
            nums1, nums2 = nums2, nums1
        # nums1中的元素最多可以减到1，nums2中的元素最多可以加到6
        diff2cnt = Counter(num - 1 for num in nums1) + Counter(6 - num for num in nums2)
        res = 0
        for d in range(5, 0, -1):
            # Counter中不存在的key会返回0
            # 注意：只要d * diff2cnt[d] >= diff，就说明能够使用若干个d以及最后一个小于等于d的数来将diff减至0。
            # 并不要求diff与d之间是整除的关系，最后减去的那个数可以是小于等于d，既然能够减去d，那么就意味着肯定也能减去小于d的数，
            # 即 最后一次操作不一定需要减到1或加到6
            if d * diff2cnt[d] >= diff:
                # res += math.ceil(diff / d)
                res += (diff - 1) // d + 1
                break
            diff -= d * diff2cnt[d]
            res += diff2cnt[d]
        return res


if __name__ == '__main__':
    print(Solution().minOperations(nums1=[6, 6], nums2=[1]))
