# -*- coding: UTF-8 -*-


class Solution:
    def appealSum(self, s: str) -> int:
        """
        动态规划。
        假设 dp[i] 表示以字符s[i]结尾的子字符串(从0开始, 长度为i+1)的总引力，那么 dp[i-1] 就表示以字符s[i-1]结尾的子字符串(从0开始, 长度为i)的总引力。
        将字符s[i]添加到以字符s[i-1]结尾的子字符串(从0开始, 长度为i)之后，将会影响到所有以字符s[i-1]结尾的子字符串(不一定从0开始, 长度小于等于i)的引力。
        若字符s[i]在以字符s[i-1]结尾的子字符串(从0开始, 长度为i)中未曾出现过，那么增加的引力为：i + 1，以字符s[i-1]结尾的子字符串共有i个，最后加上字符s[i]单独组成的子字符串；
        若字符s[i]在以字符s[i-1]结尾的子字符串(从0开始, 长度为i)中最后一次出现的下标为j，那么增加的引力为：i - 1 - j + 1，以字符s[i-1]结尾的子字符串(当中不含字符s[i])共有i - 1 - j个，最后加上字符s[i]单独组成的子字符串。
        由上可知，dp[i] 仅与 dp[i-1] 有关。
        """
        # 记录26个小写字母各自最后出现的下标。若未出现过，则将下标看作 -1。从而将上述两种情况的表达式合并为 i - j，因为 i - (-1) == i + 1
        last_idx = [-1] * 26
        res = pre = 0
        for idx, ch in enumerate(s):
            ch_idx = ord(ch) - ord('a')
            pre += idx - last_idx[ch_idx]
            res += pre
            last_idx[ch_idx] = idx
        return res


if __name__ == '__main__':
    print(Solution().appealSum(s="aa"))
