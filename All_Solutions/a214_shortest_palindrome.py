# -*- coding: UTF-8 -*-
"""
title: 最短回文串
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.


Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"


Constraints:
0 <= s.length <= 5 * 10^4
s consists of lowercase English letters only.
"""
from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        问题可转化为查找字符串s的最长回文前缀。参考LeetCode题5
        暴力枚举的时间复杂度为O(n^2)
        动态规划的时间复杂度为O(n^2)
        中心扩展算法的时间复杂度为O(n^2)
        由于s.length 最大可为 5 * 10^4，因此，O(n^2)的算法都会超时。
        Rabin-Karp字符串哈希算法的时间复杂度为O(n)，不过可能会产生哈希碰撞(概率很低)，从而导致错误的判断结果。在工程代码中，不建议这么做
        KMP算法的时间复杂度为O(n)。
        方法一：暴力枚举。实测可以通过
        """
        end = 0
        n = len(s)
        for i in range(n - 1, 0, -1):
            if s[:i + 1] == s[i::-1]:
                end = i
                break
        return s[:end:-1] + s

    def shortestPalindrome_2(self, s: str) -> str:
        """
        问题可转化为查找字符串s的最长回文前缀。
        方法二：KMP算法。
        方式一：构造一个新的字符串t = s + '#' + s'，其中，s' 为原字符串s的逆序，'#' 要求是原字符串s中不存在的特殊字符。
        然后基于字符串t 来计算前缀函数(即 next数组)，next数组中的最后一位元素就是原字符串s的最长回文前缀的长度
        """

        def get_nxt(s: str) -> List[int]:
            """前缀函数，返回next数组"""
            n = len(s)
            nxt = [0] * n
            # i、cur都是指向模式串s，i 从1开始逐步走向n-1，是因为 next[0] 必然为0，没必要计算
            # next数组可理解为：若i 与 cur所指向的字符不相等，则cur回退到 next[cur - 1]；若cur已经为0，则cur已经退无可退，cur继续为0，与第i+1个字符开始匹配。
            # 为什么cur大于0时，cur是回退到 next[cur - 1]，因为i 与 cur所指向的字符不匹配，能逐步走到这里，也就是意味着i - 1 与 cur - 1所指向的字符是匹配的，
            # 假设next[cur - 1] == j，也就表示 0 ~ j-1 与 cur - j ~ cur - 1 与 i - j ~ i - 1 这三段长度均为j的子字符串是相等的，cur回退到 next[cur - 1]，
            # 也就是说，cur = j 指向第j+1个字符，让下标为j的字符再去与下标为i的字符进行匹配，因为 0 ~ j-1 与 i - j ~ i - 1 是相同的，所以没必要让cur直接退回到0，从起点开始重新匹配。
            i = 1
            cur = 0
            # i == n时，退出循环，刚好填完next数组。只在两种情况下，会填写next数组：1、i与cur匹配成功时；2、i与cur匹配不成功时，并且cur已经回退到0了，此时的 next[i] 为0
            while i < n:
                if s[i] == s[cur]:
                    # i与cur匹配成功，所以i与cur都往前走一步，i在走之前，需要先填写next数组
                    cur += 1
                    nxt[i] = cur
                    i += 1
                elif cur > 0:
                    # cur回退到j，让下标为j的字符再去与下标为i的字符进行匹配，此时i保持不变，之后再看i与新的cur是否匹配，如果还不匹配，则让cur继续回退
                    cur = nxt[cur - 1]
                else:
                    # cur已经为0，退无可退了，只能从起点开始重新匹配了，因为当前下标为0的字符与下标为i的字符不匹配，所以跳过它，让下标为0的字符去和下标为i+1的字符进行匹配
                    # nxt[i] 的默认值就是 0
                    # nxt[i] = 0
                    i += 1
            return nxt

        nxt = get_nxt(s + '#' + s[::-1])
        prefix_len = nxt[-1]
        return s[prefix_len:][::-1] + s

    def shortestPalindrome_3(self, s: str) -> str:
        """
        问题可转化为查找字符串s的最长回文前缀。
        方法三：KMP算法。
        方式二：将原字符串s作为模式串，逆序字符串s' 作为主串。先基于原字符串s(模式串)来计算前缀函数(即 next数组)，
        然后利用next数组在逆序字符串s' (主串)中匹配模式串s，当匹配到主串s' 的最后一个字符时，若该字符对应的是模式串s的第i个字符，
        则说明原字符串s的最长回文前缀的长度为i。因为s' 与 s 是逆序，所以主串s' 的最后i个字符 与 模式串s的前i个字符也是逆序，
        然而这i个字符是匹配的(即 相同)，一个字符串等于它的逆序，也就说明这个字符串是回文。
        """

        def get_nxt(s: str) -> List[int]:
            """前缀函数，返回next数组"""
            n = len(s)
            nxt = [0] * n
            # i、cur都是指向模式串s，i 从1开始逐步走向n-1，是因为 next[0] 必然为0，没必要计算
            # next数组可理解为：若i 与 cur所指向的字符不相等，则cur回退到 next[cur - 1]；若cur已经为0，则cur已经退无可退，cur继续为0，与第i+1个字符开始匹配。
            # 为什么cur大于0时，cur是回退到 next[cur - 1]，因为i 与 cur所指向的字符不匹配，能逐步走到这里，也就是意味着i - 1 与 cur - 1所指向的字符是匹配的，
            # 假设next[cur - 1] == j，也就表示 0 ~ j-1 与 cur - j ~ cur - 1 与 i - j ~ i - 1 这三段长度均为j的子字符串是相等的，cur回退到 next[cur - 1]，
            # 也就是说，cur = j 指向第j+1个字符，让下标为j的字符再去与下标为i的字符进行匹配，因为 0 ~ j-1 与 i - j ~ i - 1 是相同的，所以没必要让cur直接退回到0，从起点开始重新匹配。
            i = 1
            cur = 0
            # i == n时，退出循环，刚好填完next数组。只在两种情况下，会填写next数组：1、i与cur匹配成功时；2、i与cur匹配不成功时，并且cur已经回退到0了，此时的 next[i] 为0
            while i < n:
                if s[i] == s[cur]:
                    # i与cur匹配成功，所以i与cur都往前走一步，i在走之前，需要先填写next数组
                    cur += 1
                    nxt[i] = cur
                    i += 1
                elif cur > 0:
                    # cur回退到j，让下标为j的字符再去与下标为i的字符进行匹配，此时i保持不变，之后再看i与新的cur是否匹配，如果还不匹配，则让cur继续回退
                    cur = nxt[cur - 1]
                else:
                    # cur已经为0，退无可退了，只能从起点开始重新匹配了，因为当前下标为0的字符与下标为i的字符不匹配，所以跳过它，让下标为0的字符去和下标为i+1的字符进行匹配
                    # nxt[i] 的默认值就是 0
                    # nxt[i] = 0
                    i += 1
            return nxt

        def get_nxt_use_for(s: str) -> List[int]:
            """使用for循环来计算next数组"""
            n = len(s)
            nxt = [0] * n
            cur = 0
            for i in range(1, n):
                while cur > 0 and s[cur] != s[i]:
                    cur = nxt[cur - 1]
                if s[cur] == s[i]:
                    cur += 1
                    nxt[i] = cur
            return nxt

        n = len(s)
        nxt = get_nxt_use_for(s)
        cur = 0
        # 利用next数组在逆序字符串s'(主串)中匹配原字符串s(模式串)
        # i 指向逆序字符串s'(主串)，cur 指向原字符串s(模式串)
        # 这里的for循环逻辑其实跟上面计算next数组的while循环逻辑基本相同，两种循环方式可以互换
        for i in range(n - 1, -1, -1):
            # 当cur大于0时，若下标为cur的字符与下标为i的字符不匹配，则让cur不断回退，直到新的cur与当前i匹配 或者 cur回退到0
            while cur > 0 and s[cur] != s[i]:
                cur = nxt[cur - 1]
            # 只有当下标为cur的字符与下标为i的字符匹配时，cur才往前走
            if s[cur] == s[i]:
                cur += 1
        return s[cur:][::-1] + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome_3("abcd"))
