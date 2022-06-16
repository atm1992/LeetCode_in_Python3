# -*- coding: UTF-8 -*-
"""
title: 复原 IP
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。


示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "1111"
输出：["1.1.1.1"]

示例 4：
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]

示例 5：
输入：s = "10203040"
输出：["10.20.30.40","102.0.30.40","10.203.0.40"]


提示：
0 <= s.length <= 3000
s 仅由数字组成
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """回溯 + 剪枝"""

        def dfs(i: int, path: List[str], cnt: int) -> None:
            if cnt == 4:
                if i == n:
                    res.append('.'.join(path))
                return
            # 剪枝
            if not 4 - cnt <= n - i <= (4 - cnt) * 3:
                return
            for j in range(i, n):
                if int(s[i:j + 1]) > 255:
                    break
                path.append(s[i:j + 1])
                dfs(j + 1, path, cnt + 1)
                path.pop()
                if j == i and s[j] == '0':
                    break

        res = []
        n = len(s)
        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("25525511135"))
