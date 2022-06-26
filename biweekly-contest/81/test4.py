# -*- coding: UTF-8 -*-


class Solution:
    def distinctSequences(self, n: int) -> int:
        dp = [[0] * 7 for _ in range(n)]
        for i in range(n):
            for j in range(1, 7):
                if i == 0:
                    dp[i][j] = 1
                elif i == 1:
                    dp[i][1] = dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6]
                    dp[i][2] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]
                    dp[i][3] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5]
                    dp[i][4] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]
                    dp[i][5] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6]
                    dp[i][6] = dp[i - 1][1] + dp[i - 1][5]
                elif i == 2:
                    dp[i][1] = dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] - dp[i - 2][
                        1] * 5
                    dp[i][2] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5] - dp[i - 2][2] * 3
                    dp[i][3] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5] - dp[i - 2][3] * 4
                    dp[i][4] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5] - dp[i - 2][4] * 3
                    dp[i][5] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6] - dp[i - 2][
                        5] * 5
                    dp[i][6] = dp[i - 1][1] + dp[i - 1][5] - dp[i - 2][6] * 2
                else:
                    dp[i][1] = dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] - dp[i - 2][
                        1] * 4
                    dp[i][2] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5] - dp[i - 2][2] * 2
                    dp[i][3] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5] - dp[i - 2][3] * 3
                    dp[i][4] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5] - dp[i - 2][4] * 2
                    dp[i][5] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6] - dp[i - 2][
                        5] * 4
                    dp[i][6] = dp[i - 1][1] + dp[i - 1][5] - dp[i - 2][6] * 1
        return sum(dp[-1]) % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().distinctSequences(4))
