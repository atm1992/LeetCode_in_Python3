# -*- coding: UTF-8 -*-
"""
title: 整数除法
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。
注意：
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31, 2^31−1]。本题中，如果除法结果溢出，则返回 2^31 − 1


示例 1：
输入：a = 15, b = 2
输出：7
解释：15/2 = truncate(7.5) = 7

示例 2：
输入：a = 7, b = -3
输出：-2
解释：7/-3 = truncate(-2.33333..) = -2

示例 3：
输入：a = 0, b = 1
输出：0

示例 4：
输入：a = 1, b = 1
输出：1


提示:
-2^31 <= a, b <= 2^31 - 1
b != 0
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        """二分查找。把a/b均转成负数，然后进行计算。因为如果都转成正数，那么-2^31转成正数后，会溢出 """
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        # 考虑特殊情况，避免溢出
        if a == INT_MIN:
            # 这里只考虑了b等于正负1的情况，在下面，a 依旧可能为INT_MIN，所以需要转成负数，而不能转成正数
            # 因为在计算过程中，不考虑sign，所以在计算过程中的中间结果(均为非负数)，INT_MIN 会被表示为 2 ** 31，从而溢出
            if b == 1:
                return INT_MIN
            # 这里会溢出，所以直接返回INT_MAX
            elif b == -1:
                return INT_MAX
        if b == INT_MIN:
            return 1 if a == INT_MIN else 0
        if a == 0:
            return 0
        # 以下为一般情况。不考虑sign的情况下，最大结果为 INT_MAX，最小结果为0。计算过程中，所有中间结果均为非负数
        sign = 1
        if a > 0:
            a = -a
            # 最终结果的符号反转一次
            sign = -sign
        if b > 0:
            b = -b
            sign = -sign

        def check(x: int, y: int, z: int) -> bool:
            """
            使用快速乘法来验证 y * z 是否大于等于x。已知：x、y为负数，结果z为正数。
            注意：y * z、x 均为负数，若y * z大于等于x，则说明 y * z 比 x 更靠近0
            若y * z大于等于x，则说明z要增大，从而使得y * z变小，逐渐接近x
            """
            res = 0
            while z:
                if z & 1:
                    # 确保res加上y以后，依旧大于等于x。如果不符合，直接就可以返回False
                    # 注意：这里写的是 res < x - y，而不是写的 res + y < x ，因为res + y有可能会溢出
                    if res < x - y:
                        return False
                    res += y
                # 若z等于1，则说明上面的res已经是最终的相乘结果了。此时没必要让y再继续乘2，避免溢出
                if z != 1:
                    # 确保y乘以2以后，依旧大于等于x。如果不符合，直接就可以返回False
                    # 跟上面一样，不写 y + y < x ，也是为了避免溢出。
                    if y < x - y:
                        return False
                    y += y
                z >>= 1
            return True

        # 最终结果z的取值范围：[0, -a]
        left, right = 0, INT_MAX if a == INT_MIN else -a
        res = 0
        while left <= right:
            # 避免溢出。注意：不能写成 left + (right - left) >> 1，这个的执行顺序是：left + (right - left) = right，然后 right >> 1
            mid = left + ((right - left) >> 1)
            # 说明z要增大
            if check(a, b, mid):
                res = mid
                # 避免之后加1溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1
        return sign * res

    def divide_2(self, a: int, b: int) -> int:
        """
        类二分查找。把a/b均转成负数，然后进行计算。因为如果都转成正数，那么-2^31转成正数后，会溢出。
        13的二进制表示为1101，即 13 = 8 + 4 + 1，所以 a = 13b = 8b + 4b + b
        先使用一个数组存储 [b, 2b, 4b, 8b, ……]，数组中的最后一个元素为最后一个小于a的倍数。注意：由于a/b都被转换成了负数，
        所以这里应该是最后一个大于a(负数)的xb。之后逆序遍历这个数组，数组下标i表示需将res的哪位二进制置为1
        """
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        # 考虑特殊情况，避免溢出
        if a == INT_MIN:
            # 这里只考虑了b等于正负1的情况，在下面，a 依旧可能为INT_MIN，所以需要转成负数，而不能转成正数
            # 因为在计算过程中，不考虑sign，所以在计算过程中的中间结果(均为非负数)，INT_MIN 会被表示为 2 ** 31，从而溢出
            if b == 1:
                return INT_MIN
            # 这里会溢出，所以直接返回INT_MAX
            elif b == -1:
                return INT_MAX
        if b == INT_MIN:
            return 1 if a == INT_MIN else 0
        if a == 0:
            return 0
        # 以下为一般情况。不考虑sign的情况下，最大结果为 INT_MAX，最小结果为0。计算过程中，所有中间结果均为非负数
        sign = 1
        if a > 0:
            a = -a
            # 最终结果的符号反转一次
            sign = -sign
        if b > 0:
            b = -b
            sign = -sign
        xb = [b]
        # 避免溢出。要求 xb[-1] + xb[-1] >= a
        while xb[-1] >= a - xb[-1]:
            xb.append(xb[-1] + xb[-1])
        res = 0
        for i in range(len(xb) - 1, -1, -1):
            if xb[i] >= a:
                res |= 1 << i
                a -= xb[i]
                if a > b:
                    break
        return sign * res


if __name__ == '__main__':
    print(Solution().divide_2(a=7, b=-3))
