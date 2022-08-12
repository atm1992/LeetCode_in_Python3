# -*- coding: UTF-8 -*-
"""
title: 最长快乐前缀
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.


Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.


Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Rabin-Karp 字符串编码
        Rabin-Karp 字符串编码是一种将字符串映射成整数的编码方式，可看成是一种哈希算法。假设字符串中包含的字符种类不超过m种，
        则可以选择一个大于等于m的质数作为base，然后就可将字符串看成base进制的整数，将其转换为10进制后，就得到了字符串对应的编码。
        这样做的好处是：可通过对比两个字符串对应的编码是否相等，来确定来个长度相同的字符串是否相同。
        其中存在的问题：字符串可能会很长，从而使得对应的编码很大，超出一般语言中的整数类型限制，
        对此的解决办法是使用一个大的质数(例如：10^9 + 7、10^9 + 9)对编码值进行取模，然后对比取模后的编码值是否相等。
        然而这会产生哈希碰撞的问题(两个原本不同的数值，取模后可能会相等)，对此的解决办法是多设置几个模数mod，
        只有两个字符串的编码值对这些mod取模后的结果都各自相等，才认为这两个字符串相同。
        不过对于一般算法题而言，只需选择一个模数即可，本题选择 mod = 10^9 + 7
        本题中的字符种类不超过26种，所以可取 base = 29
        """
        base, mod = 29, 10 ** 9 + 7
        n = len(s)
        pre_code = suf_code = 0
        idx = 0
        mul = 1
        # 最长前缀的长度不会超过n-1
        for i in range(n - 1):
            pre_code = (pre_code * base + (ord(s[i]) - ord('a'))) % mod
            suf_code = ((ord(s[n - 1 - i]) - ord('a')) * mul + suf_code) % mod
            if pre_code == suf_code:
                idx = i + 1
            mul = mul * base % mod
        return s[:idx]

    def longestPrefix_2(self, s: str) -> str:
        """KMP 算法。推荐此方法"""
        n = len(s)
        # next数组的意义：next[i] = j，表示子字符串s[:i+1]的最长前缀(同时也是最长后缀)的长度为j，即最长前缀为 s[:j]。
        # 注意：字符串(长度为n)的最长前缀不能是字符串本身，即 最长前缀的长度最大为n-1
        nxt = [0] * n
        cur = 0
        for i in range(1, n):
            while cur > 0 and s[cur] != s[i]:
                # 为什么cur大于0时，cur是回退到 next[cur-1]？
                # 因为i与cur所指向的字符不匹配，能逐步走到这里，也就是意味着i-1与cur-1所指向的字符是匹配的，
                # 假设next[cur-1] = j，也就表示 0 ~ j-1 与 cur-j ~ cur-1 与 i-j ~ i-1 这三段长度均为j的子字符串是相等的，
                # cur回退到next[cur-1]之后，让下标为j的字符再去与下标为i的字符进行匹配，因为 0 ~ j-1 与 i-j ~ i-1 是相同的，
                # 所以没必要让cur直接回退到0，从起点开始重新匹配。
                cur = nxt[cur - 1]
            if s[cur] == s[i]:
                cur += 1
                # cur先加1再填写next数组，是因为next数组中记录的是最长前缀的长度，长度需要在下标的基础上加1
                nxt[i] = cur
        return s[:nxt[-1]]


if __name__ == '__main__':
    print(Solution().longestPrefix_2('level'))
