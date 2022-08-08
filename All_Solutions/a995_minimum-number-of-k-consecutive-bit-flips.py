# -*- coding: UTF-8 -*-
"""
title: K 连续位的最小翻转次数
You are given a binary array nums and an integer k.
A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:
Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation:
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]


Constraints:
1 <= nums.length <= 10^5
1 <= k <= nums.length
"""
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        差分数组
        普通模拟(贪心)：从左往右遍历nums，若当前元素i为0，则说明当前元素i必须翻转一次，因此翻转nums[i:i+k]，然后继续往后遍历(注意：是遍历翻转后的最新值，而不是最初的原始值)，
        遇到0就翻转一次当前元素及后面的k-1个元素。最后如果0所在的位置后面不足k-1个元素，则说明不可能完成翻转，因此返回-1
        上述过程中，其实可以不对元素进行实际的翻转，而是记录每个元素已被翻转的次数，即 前面k-1个元素的翻转次数累加和，因为只有前面k-1个元素的翻转才会连带翻转当前元素。
        存在以下两种情况，当前元素是需要翻转的：
        1、若当前元素已被翻转的次数为偶数，且当前元素为0，0翻转偶数次后，依旧是0，所以当前元素必须再翻转一次；
        2、若当前元素已被翻转的次数为奇数，且当前元素为1，1翻转奇数次后，将会变成0，所以当前元素也必须再翻转一次。
        这两种情况可以统一为：(reverse_cnt + nums[i]) % 2 == 0
        计算当前元素已被翻转的次数时，每次翻转都需要将nums[i] ~ nums[i+k-1]的翻转次数加1，每次操作的时间复杂度均为O(k)。
        可使用差分数组diff来降低该操作的时间复杂度，diff[i] = nums[i]的翻转次数 - nums[i-1]的翻转次数。
        翻转区间[i, i+k-1]时，nums[i] ~ nums[i+k-1]的翻转次数均加1 可转换为 diff[i+1] ~ diff[i+k-1]的值保持不变，diff[i]加1，diff[i+k]减1
        通过累加差分数组diff就可得到当前元素已被翻转的次数reverse_cnt[i] = (reverse_cnt[i] - reverse_cnt[i-1]) + (reverse_cnt[i-1] - reverse_cnt[i-2])
                                                                    + …… + (reverse_cnt[1] - reverse_cnt[0]) + (reverse_cnt[0] - 0)
                                                                = diff[i] + diff[i-1] + …… + diff[1] + diff[0]
        """
        n = len(nums)
        # 差分数组diff中是可能存在负数的
        diff = [0] * (n + 1)
        res = reverse_cnt = 0
        for i in range(n):
            # reverse_cnt 表示当前元素nums[i]已被翻转的次数，reverse_cnt始终大于等于0
            reverse_cnt += diff[i]
            # 需要翻转当前元素及后面的k-1个元素
            if (reverse_cnt + nums[i]) % 2 == 0:
                if i + k > n:
                    return -1
                # 因为diff[i]之后不会再被使用，所以可以不用修改diff[i]
                # diff[i] += 1
                diff[i + k] -= 1
                res += 1
                # 注意：别忘了这行代码，因为当前元素又翻转了一次，所以reverse_cnt需要加1
                reverse_cnt += 1
        return res

    def minKBitFlips_2(self, nums: List[int], k: int) -> int:
        """
        差分数组。优化方法一，因为只需关注当前元素已被翻转的次数reverse_cnt的奇偶性，所以可用0/1来表示reverse_cnt，异或运算可实现不进位的相加。
        """
        n = len(nums)
        # 差分数组diff中是可能存在负数的
        diff = [0] * (n + 1)
        res = reverse_cnt = 0
        for i in range(n):
            reverse_cnt ^= diff[i]
            if reverse_cnt == nums[i]:
                if i + k > n:
                    return -1
                diff[i + k] ^= 1
                res += 1
                reverse_cnt ^= 1
        return res

    def minKBitFlips_3(self, nums: List[int], k: int) -> int:
        """
        滑动窗口
        上述方法中的差分数组diff其实可省略，从而降低空间复杂度。
        观察上述 reverse_cnt ^= diff[i] 对reverse_cnt的修改，会发现只有当diff[i]从默认值0变成了1时，才会修改reverse_cnt，因为 reverse_cnt ^ 0 = reverse_cnt
        而又知道只有翻转元素i-k时，才会修改diff[i]，所以只要知道元素i-k是否被翻转过，就能知道是否需要修改reverse_cnt，即 reverse_cnt ^ 1

        因为nums中只有0或1，所以可使用一个其它值来表示某个元素是否被翻转过，例如：若要翻转nums[i] ~ nums[i+k-1]，则可将nums[i]加2，
        之后遍历到nums[i+k]时，因为nums[i+k - k]大于1，所以可知nums[i]被翻转过
        """
        n = len(nums)
        res = reverse_cnt = 0
        for i in range(n):
            if i >= k and nums[i - k] > 1:
                reverse_cnt ^= 1
                # 恢复元素的值
                nums[i - k] -= 2
            if reverse_cnt == nums[i]:
                if i + k > n:
                    return -1
                nums[i] += 2
                res += 1
                reverse_cnt ^= 1
        return res
