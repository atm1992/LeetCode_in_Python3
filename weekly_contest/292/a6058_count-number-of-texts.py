# -*- coding: UTF-8 -*-


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        """
        分组DP。dp[i] 表示以pressKey[i]结尾的方案个数，其中dp[0]=1
        分情况讨论状态转移方程：
        1、若pressedKeys[i] != pressedKeys[i-1]，则 dp[i]=dp[i-1]，可理解为在长度为i-1的字符串后面加了一个字符i(固定字母)，此时方案数不变
        2、若pressedKeys[i] == pressedKeys[i-1]，则 dp[i]=dp[i-1] + dp[i-2]，可理解为在长度为i-1的字符串后面加了一个字符i，只不过这个字符与字符i-1相同，
        此时的方案数为dp[i-1]；另外，字符i 与 字符i-1可以合并组成一个新字母，然后接到长度为i-2的字符串后面，此时的方案数为dp[i-2]
        3、若pressedKeys[i] == pressedKeys[i-1] == pressedKeys[i-2]，则 dp[i]=dp[i-1] + dp[i-2] + dp[i-3]，可理解为 情况2的基础上，
        字符i、字符i-1、字符i-2合并组成一个新字母，然后接到长度为i-3的字符串后面，此时的方案数为dp[i-3]
        4、若pressedKeys[i] == pressedKeys[i-1] == pressedKeys[i-2] == pressedKeys[i-3]，且字符为7或9，则 dp[i]=dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]，
        可理解为 情况3的基础上，字符i、字符i-1、字符i-2、字符i-3合并组成一个新字母，然后接到长度为i-4的字符串后面，此时的方案数为dp[i-4]
        5、以情况2为例，假设pressedKeys[i] == pressedKeys[i-1]，i = 1，即 i < 2，此时dp[i-2]不存在，则认为dp[i-2]=1，
        表示在长度为i-1的字符串后面加了一个字符i，此时方案数为dp[i-1]；然后，字符i 与 字符i-1合并组成一个字母，此时的方案数为1
        """
        mod = 10 ** 9 + 7
        n = len(pressedKeys)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            # 无论哪种情况，dp[i]都大于等于dp[i-1]
            val = dp[i - 1]
            ch = pressedKeys[i]
            if ch == pressedKeys[i - 1]:
                val += dp[i - 2] if i >= 2 else 1
                if i >= 2 and ch == pressedKeys[i - 2]:
                    val += dp[i - 3] if i >= 3 else 1
                    if i >= 3 and ch == pressedKeys[i - 3] and ch in ['7', '9']:
                        val += dp[i - 4] if i >= 4 else 1
            dp[i] = val % mod
        return dp[-1]


if __name__ == '__main__':
    print(Solution().countTexts("222222222222222222222222222222222222"))
