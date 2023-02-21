# -*- coding: UTF-8 -*-
"""
title: 破解保险箱
There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].
The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.
    For example, the correct password is "345" and you enter in "012345":
        After typing 0, the most recent 3 digits is "0", which is incorrect.
        After typing 1, the most recent 3 digits is "01", which is incorrect.
        After typing 2, the most recent 3 digits is "012", which is incorrect.
        After typing 3, the most recent 3 digits is "123", which is incorrect.
        After typing 4, the most recent 3 digits is "234", which is incorrect.
        After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.
Return any string of minimum length that will unlock the safe at some point of entering it.


Example 1:
Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.

Example 2:
Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4th digit.
- "01" is typed in starting from the 1st digit.
- "10" is typed in starting from the 3rd digit.
- "11" is typed in starting from the 2nd digit.
Thus "01100" will unlock the safe. "01100", "10011", and "11001" would also unlock the safe.


Constraints:
1 <= n <= 4
1 <= k <= 10
1 <= k^n <= 4096
"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        Hierholzer算法求解欧拉回路
        若将所有的n-1位数作为节点，则总共有 k^(n-1) 个节点，每个节点都有k条入边和k条出边，假设每条出边的编号为0 ~ k-1，
        则每个节点加上一条出边的编号就是一种密码序列，总共有 k^(n-1) * k = k^n 种密码序列

        欧拉回路：从任意一个节点开始，一次性不重复地走完所有的边且回到该节点。

        Hierholzer算法：从任意一个节点u开始，任意地经过还未经过的边，直到无路可走，则此时一定回到了节点u，因为所有节点的入度和出度都相等。
        回到节点u之后，就得到了一条从u开始到u结束的回路，这条回路上仍然有些节点有未经过的出边。然后从这些节点中选一个节点v开始，
        继续得到一条从v开始到v结束的回路，把这条回路嵌入到之前的回路中，即 u -> …… -> v -> …… -> u  变为  u -> …… -> v -> …… -> v -> …… -> u
        以此类推，直到没有节点有未经过的出边，此时就找到了一条欧拉回路
        可以验证，最终的序列长度一定为 k^n + (n-1)
        """
        visited = set()
        res = []
        # 用于取余，得到最后n-1位数
        mod = 10 ** (n - 1)

        def dfs(cur: int) -> None:
            for x in range(k):
                nxt = cur * 10 + x
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt % mod)
                    res.append(str(x))

        dfs(0)
        return ''.join(res) + '0' * (n - 1)


if __name__ == '__main__':
    print(Solution().crackSafe(n=3, k=2))
