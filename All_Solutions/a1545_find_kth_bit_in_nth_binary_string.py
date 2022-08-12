# -*- coding: UTF-8 -*-
"""
title: 找出第 N 个二进制字符串中的第 K 位
Given two positive integers n and k, the binary string Sn is formed as follows:
    S1 = "0"
    Si = S(i-1) + "1" + reverse(invert(S(i-1))) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.


Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".

Example 2:
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

Example 3:
Input: n = 1, k = 1
Output: "0"

Example 4:
Input: n = 2, k = 3
Output: "1"


Constraints:
1 <= n <= 20
1 <= k <= 2^n - 1
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """模拟"""
        pre = '0'
        for _ in range(1, n):
            tmp = []
            for ch in pre:
                tmp.append(str(1 - int(ch)))
            pre = pre + '1' + ''.join(tmp[::-1])
        return pre[k - 1]

    def findKthBit_2(self, n: int, k: int) -> str:
        """
        递归。执行效率远高于上面
        由题意可知，len(Si) = 2 * len(S(i-1)) + 1，len(S1) = 1。所以，len(Sn) = 2^n - 1
        第一个字符一定为'0'，所以k=1时，直接返回'0'。这里可以把n=1的情况拦截掉
        以下考虑n>1的情况：
        1、若k = 2^(n-1)，则所求字符为最中间那个字符，已知最中间那个字符为'1'，因此直接返回'1'
        2、若k < 2^(n-1)，则所求字符为S(i-1)中的第k个字符，即 findKthBit(n-1, k)
        3、若k > 2^(n-1)，则所求字符为S(i-1)中的第2^n - k个字符的翻转字符，即 str(1 - int(findKthBit(n-1, 2^n - k)))
        """
        if k == 1:
            return '0'
        mid = 1 << (n - 1)
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit_2(n - 1, k)
        else:
            return str(1 - int(self.findKthBit_2(n - 1, (1 << n) - k)))


if __name__ == '__main__':
    print(Solution().findKthBit_2(n=4, k=11))
