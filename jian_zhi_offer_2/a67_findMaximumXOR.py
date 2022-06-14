# -*- coding: UTF-8 -*-
"""
title: 最大的异或
给定一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。


示例 1：
输入：nums = [3,10,5,25,2,8]
输出：28
解释：最大运算结果是 5 XOR 25 = 28.

示例 2：
输入：nums = [0]
输出：0

示例 3：
输入：nums = [2,4]
输出：6

示例 4：
输入：nums = [8,10,2]
输出：10

示例 5：
输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
输出：127


提示：
1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2^31 - 1

进阶：你可以在 O(n) 的时间解决这个问题吗？
"""
from typing import List


class Trie:
    def __init__(self):
        # 二进制位要么为1、要么为0，所以这里的字典树其实是一棵二叉树，高度为32(包含root)
        # left指向表示 0 的子节点
        self.left = None
        # right指向表示 1 的子节点
        self.right = None


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """暴力。运行超时，通过 33/41 个测试用例"""
        res = 0
        n = len(nums)
        # n1 ^ n2 == n2 ^ n1
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, nums[i] ^ nums[j])
        return res

    def findMaximumXOR_4(self, nums: List[int]) -> int:
        """优化暴力。运行超时，通过 38/41 个测试用例"""
        res = 0
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n - 1):
            if nums[i] + nums[i + 1] <= res:
                break
            for j in range(i + 1, n):
                # 异或可看作是不进位的相加。如果两个数直接相加都不大于当前最大的异或结果，那它们的异或结果一定不大于当前最大的异或结果。
                # 又因为nums降序了，后面的数只会越来越小
                if nums[i] + nums[j] <= res:
                    break
                res = max(res, nums[i] ^ nums[j])
        return res

    def findMaximumXOR_2(self, nums: List[int]) -> int:
        """
        哈希表 + 贪心。推荐使用此方法
        要使res尽可能大，也就意味着尽可能使res的高二进制位为1。已知nums[i] <= 2^31 - 1，即 num 最大为31位1，因此res也只可能最大为31位1。
        所以可以从高位(第31位)向低位(第1位)来逐个确定res的各个二进制位能否为1，尽量满足高二进制位为1，即 贪心思想
        res = n1 ^ n2  ————>  n2 = n1 ^ res
        """
        res = 0
        # 从右移30位(只保留最高位)到右移0位(原始num)
        for i in range(30, -1, -1):
            # 这里面保存的是n2，用于确定是否存在想要的n2
            pre_i_bit = set()
            for n2 in nums:
                # 初始时，右移30位，只保留第31位的值
                pre_i_bit.add(n2 >> i)
            # 2 * res 表示先将之前位的验证结果左移一位(固化下来)，后面的 +1 表示现在需要验证res的当前二进制位能否为1，先把res的该位置1
            # 因为res中一直带着之前位的验证结果，所以不存在说某个n2只能使res的当前位为1，而不能通过res之前位的验证。
            res = 2 * res + 1
            found = False
            for n1 in nums:
                # 这里验证的是res从最高位到当前位，是否存在想要的n2，不单单是要求使res的当前位为1
                if (n1 >> i) ^ res in pre_i_bit:
                    found = True
                    break
            # 如果遍历完所有的n1，也不能找到想要的n2，就说明res的当前二进制位不能为1，所以需要把之前置的1变回0
            if not found:
                res -= 1
        return res

    def findMaximumXOR_3(self, nums: List[int]) -> int:
        """字典树。综合方法一和方法二，再加上字典树。方法二的时间复杂度为O(31 * n * 2)，方法三的时间复杂度为O(n * 31 * 2)"""
        root = Trie()

        def insert(num: int) -> None:
            node = root
            for i in range(30, -1, -1):
                if (num >> i) & 1:
                    if not node.right:
                        node.right = Trie()
                    node = node.right
                else:
                    if not node.left:
                        node.left = Trie()
                    node = node.left

        def get_xor_max(num: int) -> int:
            """在当前的字典树中，查找与输入num的最大异或结果"""
            node = root
            tmp = 0
            for i in range(30, -1, -1):
                # 验证tmp的当前二进制位之前，先将之前位的验证结果左移一位(固化下来)
                tmp <<= 1
                # 若输入num的当前二进制位为1，则应该查找当前位上是否有0(left)，这样才能使得异或结果tmp的当前位为1
                if (num >> i) & 1:
                    if node.left:
                        # tmp的当前二进制位可以为1
                        tmp += 1
                        node = node.left
                    else:
                        # 因为之前insert的每个num都是31位(高位补0)，所以左、右两个子节点，必然会存在一个
                        node = node.right
                else:
                    if node.right:
                        tmp += 1
                        node = node.right
                    else:
                        node = node.left
            return tmp

        res = 0
        for i in range(1, len(nums)):
            # 先将前一个num插入到字典树，然后用当前num与之前的所有num分别异或(与方法一不同的是，无论之前的num有多少个，时间复杂度都是固定的常数级别，
            # 因为字典树的高度固定为32(包含root))，查找出最大的异或结果
            insert(nums[i - 1])
            res = max(res, get_xor_max(nums[i]))
        return res


if __name__ == '__main__':
    print(Solution().findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
