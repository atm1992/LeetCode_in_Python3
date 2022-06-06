# -*- coding: UTF-8 -*-
"""
title: 值和下标之差都在给定的范围内
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
如果存在则返回 true，不存在返回 false。


示例 1：
输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1, t = 2
输出：true

示例 3：
输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false


提示：
0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1
"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """"
        利用桶排序的思想，对元素按大小进行分桶。
        桶ID为：nums[i] // (t + 1)
        假设t=9，则 0 ~ 9 会被分配到id为 0 的桶； -10 ~ -1 会被分配到id为 -1 的桶 …… 。abs(-10 - -1) == 9 <= t
        同一个桶中的元素，一定满足 abs(nums[i] - nums[j]) <= t 。若是相邻桶，则需比较大小。
        优化：一个桶中只需保存遇到的第一个元素，也就是说，value是一个值，而不是一个列表。
        可行原因：
        1、如果后续遍历，遇到同属一个桶的元素，则直接返回True，无需继续遍历了
        2、比较相邻桶时，也无需担心某些更相近的元素之前没加入到相邻桶，原因就是上面说的，如果存在属于相邻桶的更相近的元素，那么之前就已经return True了，
        根本不会遍历到现在，之所以能够遍历到现在，就是因为相邻桶自从加入了第一个元素后，一直也没遇到同属该桶的元素。
        """

        def get_id(num: int) -> int:
            """
            需要注意的是，Python中负数的整除、取余与Java/C++中不一样。Python在这块与日常理解不太一样！
            Python中的负数整除：-1 // 10 == -10 // 10 == -1        -11 // 10 == -2
            Java/C++中的负数整除：-1 // 10 == -9 // 10 == 0        -10 // 10 == -11 // 10 == -1
            所以，对于负数，Java/C++中需要写成：(num + 1) // (t + 1) - 1
            (num + 1)： -1 ~ -10 ——> 0 ~ -9
            // (t + 1)：0 ~ -9  ——> 0 // 10 == -9 // 10 == 0
             - 1：0 ——> -1
            最终实现：-1 // 10 == -10 // 10 == -1
            所以，Python中若想实现正常的负数整除：int(num / 10)     # 正负数整除都可以用这种方式，利用int()向0的方向取整，并不是单纯的向下取整

            Python中的负数取余：-1 % 10 == 9       -9 % 10 == 1        -10 % 10 == 0       -11 % 10 == 9
            Java/C++中的负数取余：-1 % 10 == -1    -9 % 10 == -9       -10  % 10 == 0      -11  % 10 == -1
            所以，Python中若想实现正常的负数取余：-(-num % 10)      # 负数取余用这种方式，正数取余还是用常规的 num % 10
            """
            return num // (t + 1)

        if len(nums) < 2 or k == 0:
            return False
        id2num = {}
        for idx, num in enumerate(nums):
            id = get_id(num)
            if id in id2num:
                return True
            if id - 1 in id2num and abs(id2num[id - 1] - num) <= t:
                return True
            if id + 1 in id2num and abs(id2num[id + 1] - num) <= t:
                return True
            id2num[id] = num
            if idx >= k:
                id2num.pop(get_id(nums[idx - k]))
        return False
