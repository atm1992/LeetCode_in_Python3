# -*- coding: UTF-8 -*-
"""
title: 所有子集
给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。


示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]


提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯"""
        res = []
        n = len(nums)

        def dfs(i: int, path: List[int]) -> None:
            if i == n:
                res.append(path[:])
                return
            # 选择当前元素
            path.append(nums[i])
            dfs(i + 1, path)
            # 回溯
            path.pop()

            # 跳过当前元素
            dfs(i + 1, path)

        dfs(0, [])
        return res

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        """使用二进制位进行枚举。n位全0，表示所有元素都不选，即 []；n位全1，表示全选所有元素，即 nums本身。
        n为数组nums的长度，从0遍历到2^n - 1，就可取到所有的子集。"""
        n = len(nums)
        res, tmp = [], []
        for mask in range(2 ** n):
            tmp.clear()
            i = 0
            while mask > 0:
                if mask & 1:
                    tmp.append(nums[i])
                i += 1
                mask >>= 1
            res.append(tmp[:])
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
