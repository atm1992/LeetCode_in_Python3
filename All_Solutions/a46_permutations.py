# -*- coding: UTF-8 -*-
"""
title: 全排列
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯。使用visited数组或二进制位来标记某个数字是否已使用过，可以让返回结果中数字的顺序与原始nums中的顺序一致"""

        def dfs(idx: int = 0, path: List[int] = [], visited: int = 0) -> None:
            """idx 表示当前要填入path数组中哪个位置(0 ~ n-1)的元素"""
            if idx == n:
                # 这里无需copy path，因为每次递归调用时，传入的都是一个新的path数组
                res.append(path)
                return
            for i in range(n):
                if (visited >> i) & 1 == 0:
                    # 每次递归都会创建中间变量。并不直接修改原始变量idx、path、visited，而是以它们为基础，创建新的变量
                    dfs(idx + 1, path + [nums[i]], visited | (1 << i))

        n = len(nums)
        res = []
        dfs()
        return res

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        """回溯。省略visited数组或二进制位，不考虑返回结果中数字的顺序；也不使用path数组，直接修改原始nums中的顺序，降低空间复杂度"""

        def dfs(idx: int = 0) -> None:
            if idx == n:
                # 从头到尾只使用原始的nums数组，也不在递归过程中创建中间变量。
                # 所以这里需要进行copy，避免在后续的递归过程中，修改了结果数组res中的子数组
                res.append(nums[:])
                # 这里不写return，其实也可以。因为下面的for i in range(n, n)并不会进入执行，然后会隐式return
                return
            # idx 依次指向子数组中的某个位置(下标为0~n-1)，表示当前需要确定哪个位置上的元素。
            # 0 ~ idx-1是已选择元素，idx ~ n-1是可选择元素。从idx ~ n-1中选一个合适的元素放到idx位置上，这样就不可能会有重复元素
            for i in range(idx, n):
                # 交换位置i和位置idx上的元素。表示将nums[i]放到位置idx上，然后递归确定位置idx+1上的元素
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx + 1)
                # 回溯时撤销前面的元素交换
                nums[i], nums[idx] = nums[idx], nums[i]

        n = len(nums)
        res = []
        dfs()
        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
