# -*- coding: UTF-8 -*-
"""
title: 计算右侧小于当前元素的个数
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].


Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        离散化 + 树状数组 or 线段树。此题场景更适合树状数组。逆序遍历nums，使用树状数组记录每个元素的出现次数
        离散化：先用set对nums去重，然后转成升序数组，接着将每个元素值与idx做映射，之后根据idx(通过num获取)去更新树状数组(or 线段树)中的出现次数
        树状数组(or 线段树)：根据升序数组的长度(初始时，所有元素的出现次数均为0)去构建树状数组，之后使用树状数组 获取前缀和 以及 给当前元素的出现次数加1
        """
        sorted_nums = sorted(set(nums))
        num2idx = {}
        for idx, num in enumerate(sorted_nums):
            num2idx[num] = idx

        # 树状数组的下标从1开始，下标0不使用，保持为默认值0
        # 这里并不需要初始化树状数组，因为初始时所有元素的出现次数均为0
        bit = [0] * (len(sorted_nums) + 1)
        bit_size = len(bit)

        def low_bit(idx: int) -> int:
            return idx & -idx

        def bit_add_1(idx: int) -> None:
            """给指定idx的元素加1，出现次数加1"""
            # 树状数组的下标从1开始
            idx += 1
            while idx < bit_size:
                bit[idx] += 1
                idx += low_bit(idx)

        def bit_pre_sum(idx: int) -> int:
            """获取指定idx及之前所有元素的累加和"""
            res = 0
            # 树状数组的下标从1开始
            idx += 1
            while idx > 0:
                res += bit[idx]
                idx -= low_bit(idx)
            return res

        n = len(nums)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            num = nums[i]
            idx = num2idx[num]
            # 通过树状数组获取小于当前num的所有元素的出现次数
            res[i] = bit_pre_sum(idx - 1)
            # 当前num的出现次数加1
            bit_add_1(idx)
        return res

    def countSmaller_2(self, nums: List[int]) -> List[int]:
        """
        归并排序 + 索引数组。解法类似于 剑指 Offer 51. 数组中的逆序对。更推荐使用树状数组
        使用索引数组记录原数组在归并排序过程中的下标变化
        归并排序前：  nums = [8, 9, 1, 5, 2]
                    idxs = [0, 1, 2, 3, 4]
        归并排序后：  nums = [1, 2, 5, 8, 9]
                    idxs = [2, 4, 3, 0, 1]
        """
        n = len(nums)
        idxs = list(range(n))
        # 归并排序过程中，临时记录nums、idxs的变化。每次merge合并完成后，都将这些变化覆盖回nums、idxs
        tmp_nums = [0] * n
        tmp_idxs = [0] * n
        res = [0] * n

        def merge_sort(nums: List[int], left: int, right: int) -> None:
            # 0个或1个元素
            if left >= right:
                return
            mid = (left + right) >> 1
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)
            merge(nums, left, mid, right)

        def merge(nums: List[int], left: int, mid: int, right: int) -> None:
            """重点在于归并排序的合并过程"""
            # 前后两段有序子数组的起始下标
            i, j = left, mid + 1
            # 合并后完整数组的起始下标
            p = left
            while i <= mid and j <= right:
                # 说明后边那段有序子数组中存在 j-1-mid 个元素是小于nums[i]的
                if nums[i] <= nums[j]:
                    # 获取nums[i]这个元素值在原数组nums中的下标，因为nums、idxs这两个数组是同步变化的
                    idx = idxs[i]
                    # 将加入nums[i]到合并后的数组
                    tmp_nums[p] = nums[i]
                    # 同步更新idxs
                    tmp_idxs[p] = idx
                    res[idx] += j - 1 - mid
                    i += 1
                    p += 1
                else:
                    idx = idxs[j]
                    # 将加入nums[j]到合并后的数组
                    tmp_nums[p] = nums[j]
                    # 同步更新idxs
                    tmp_idxs[p] = idx
                    j += 1
                    p += 1
            while i <= mid:
                # 获取nums[i]这个元素值在原数组nums中的下标，因为nums、idxs这两个数组是同步变化的
                idx = idxs[i]
                # 将加入nums[i]到合并后的数组
                tmp_nums[p] = nums[i]
                # 同步更新idxs
                tmp_idxs[p] = idx
                res[idx] += j - 1 - mid
                i += 1
                p += 1
            while j <= right:
                idx = idxs[j]
                # 将加入nums[j]到合并后的数组
                tmp_nums[p] = nums[j]
                # 同步更新idxs
                tmp_idxs[p] = idx
                j += 1
                p += 1
            # 每次merge合并完成后，都将这些变化覆盖回nums、idxs
            nums[left:right + 1] = tmp_nums[left:right + 1]
            idxs[left:right + 1] = tmp_idxs[left:right + 1]

        # 调用结束后，原数组nums将变为升序
        merge_sort(nums, 0, n - 1)
        # print(nums)
        # print(idxs)
        return res


if __name__ == '__main__':
    print(Solution().countSmaller_2([5, 2, 6, 1]))
