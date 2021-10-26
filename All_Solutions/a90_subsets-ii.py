# -*- coding: UTF-8 -*-
"""
title: 子集 II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """回溯。先对nums排序，递归时，若发现未选择上一个数，且上一个数等于当前数字，则跳过当前生成的子集"""

        def dfs(idx: int = 0, choose_pre: bool = False, path: list = []):
            if idx == n:
                res.append(path[:])
                return
            # 跳过当前元素
            dfs(idx + 1, False, path)
            # 这个主要在跳过所有元素后，回溯时起作用
            if not choose_pre and idx > 0 and nums[idx - 1] == nums[idx]:
                return

            # 选择当前元素
            path.append(nums[idx])
            dfs(idx + 1, True, path)
            path.pop()

        nums.sort()
        n = len(nums)
        res = []
        dfs()
        return res

    def subsetsWithDup_2(self, nums: List[int]) -> List[List[int]]:
        """使用二进制位进行枚举。n位全0，表示所有元素都不选，即 []；n位全1，表示全选所有元素，即 nums本身。
        n为数组nums的长度，从0遍历到2^n - 1，就可取到所有的子集。
        先对nums排序，迭代时，若发现未选择上一个数，且上一个数等于当前数字，则跳过当前生成的子集"""
        nums.sort()
        n = len(nums)
        res, tmp = [], []
        for mask in range(2 ** n):
            tmp.clear()
            idx = 0
            ignore = False
            # 初始值为mask最低bit位的值
            pre_bit = mask % 2
            while mask > 0:
                cur_bit = mask & 1
                if cur_bit:
                    # 进入到判断 not pre_bit 时，idx一定是大于0的。因为pre_bit的初始值就是mask最低bit位，
                    # 即 idx==0 时，pre_bit = cur_bit
                    if not pre_bit and nums[idx - 1] == nums[idx]:
                        ignore = True
                        break
                    tmp.append(nums[idx])
                idx += 1
                pre_bit = cur_bit
                mask >>= 1
            if not ignore:
                res.append(tmp[:])
        return res


if __name__ == '__main__':
    print(Solution().subsetsWithDup(nums=[5, 5, 5, 5, 5]))
