# -*- coding: UTF-8 -*-
"""
title: 统计打字方案数
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.
In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.
    For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
    Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.
    For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.
Since the answer may be very large, return it modulo 109 + 7.


Example 1:
Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.

Example 2:
Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.


Constraints:
1 <= pressedKeys.length <= 10^5
pressedKeys only consists of digits from '2' - '9'.
"""


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
