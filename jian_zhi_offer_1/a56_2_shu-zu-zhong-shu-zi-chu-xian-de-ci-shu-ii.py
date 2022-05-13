# -*- coding: UTF-8 -*-
"""
title: 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。


示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1


限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
"""
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """哈希表"""
        for num, cnt in Counter(nums).items():
            if cnt == 1:
                return num

    def singleNumber_2(self, nums: List[int]) -> int:
        """
        分别统计每一位上1的个数，然后对3取余。该方法适用于所有的 一个数字出现一次，其余数字出现n次（对n取余）类问题
        Python不区分 有符号整数类型 和 无符号整数类型，所以对于负数，Python需要特殊处理。不过，注意到1 <= nums[i] < 2^31，意味着无需考虑负数
        """
        res = 0
        # 用32位来表示一个int整数，分别统计每一位上1的个数
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                res |= 1 << i
        return res

    def singleNumber_3(self, nums: List[int]) -> int:
        """
        有限状态自动机(数字电路设计)。负数也适用
        # 遍历数组，统计每个bit位上1的出现次数时，对于任一bit位，其统计结果都是 0 ——> 1 ——> 2 ——> 0（%3），转换为二进制便是 00 ——> 01 ——> 10 ——> 00
        # 因此可用两个int整数（twos、ones）来表示每个bit位上1的统计结果。以 最右位的统计结果为01 为例，则可表示成twos的最右位为0、ones的最右位为1
        # 统计过程可描述如下：
        #    1、遍历数组中的数字，统计结果以最右位为例。twos、ones的初始值均为0
        #    2、若第一个数字的最右位为1，则此时twos的最右位为0、ones的最右位为1
        #    3、若第二个数字的最右位也为1，则此时twos的最右位为1、ones的最右位为0
        #    4、若第三个数字的最右位也为1，则此时twos的最右位为0、ones的最右位为0
        #    5、……
        # 异或可以实现不进位的相加，0+0=0;0+1=1;1+0=1;1+1=0。即 ones = ones ^ num; twos = twos ^ num
        # twos、ones不会同时为1，当ones为1时，twos必为0；当ones为0时，twos可以为1。即 ones = ones & ~twos; twos = twos & ~ones
        # 最终统计结果一定是01，即 twos的所有位均为0、ones等于要查找的那个出现一次的数字
        """
        ones, twos = 0, 0
        for num in nums:
            # 下面这两句的顺序不能换，先计算低位，再计算高位。先把num不进位加到ones上
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
