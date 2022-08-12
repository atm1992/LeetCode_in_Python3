# -*- coding: UTF-8 -*-
"""
title: 含最多 K 个可整除元素的子数组
Given an integer array nums and two integers k and p, return the number of distinct subarrays which have at most k elements divisible by p.
Two arrays nums1 and nums2 are said to be distinct if:
    They are of different lengths, or
    There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.


Example 1:
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11
Explanation:
The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.

Example 2:
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation:
All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.


Constraints:
1 <= nums.length <= 200
1 <= nums[i], p <= 200
1 <= k <= nums.length
"""
from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """暴力破解 + set去重"""
        res = set()
        n = len(nums)
        for start in range(n):
            cnt = 0
            for end in range(start, n):
                if nums[end] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                res.add(tuple(nums[start: end + 1]))
        return len(res)

    def countDistinct_2(self, nums: List[int], k: int, p: int) -> int:
        """字典树。每产生一个不同的子数组，必将会在字典树中插入一个新节点。最终答案 = 字典树中新插入的节点数量"""
        # 根节点初始时，为一个空dict
        trie = [{}]

        def insert_node() -> int:
            # 新加一个空节点
            trie.append({})
            # 返回新加节点在trie数组中的下标
            return len(trie) - 1

        for i in range(len(nums)):
            cnt = 0
            # 每次都是从根节点开始找
            node_idx = 0
            for num in nums[i:]:
                if num % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                if num not in trie[node_idx]:
                    trie[node_idx][num] = insert_node()
                node_idx = trie[node_idx][num]
        # 需要除去根节点
        return len(trie) - 1


if __name__ == '__main__':
    print(Solution().countDistinct_2(nums=[2, 3, 3, 2, 2], k=2, p=2))
