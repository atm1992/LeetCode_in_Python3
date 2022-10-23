# -*- coding: UTF-8 -*-
"""
title: 安卓系统手势解锁
Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:
    All the dots in the sequence are distinct.
    If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
        For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.
        However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.
Here are some example valid and invalid unlock patterns:
    The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
    The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
    The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
    The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.
Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.
Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.


Example 1:
Input: m = 1, n = 1
Output: 9

Example 2:
Input: m = 1, n = 2
Output: 65


Constraints:
1 <= m, n <= 9
"""
from functools import lru_cache


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        DFS + 状态压缩 + 记忆化
        先列出所有不能直接到达的情况，剩下的就都是可以直接到达的情况。
        对所有不能直接到达的情况进行分析发现：1、3、7、9是类似的情况，从1出发的解锁模式数量会等于从3出发的；同理，2、4、6、8也是类似的；5是个特例。
        所以最终结果为：从1出发的数量 * 4 + 从2出发的数量 * 4 + 从5出发的数量。
        因为总共只有9个数字，所以可使用一个int值的二进制位来表示已使用过的数字。例如：1 << 2 表示数字2已被使用过
        """
        # 所有不能直接到达的情况，到达之前，必须经过了中间点。除了下面这些情况，都是可以直接到达的
        graph = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: {},
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8}
        }

        @lru_cache(maxsize=None)
        def dfs(pre: int, size: int, status: int) -> int:
            """
            :param pre: 上一个数字
            :param size: 解锁序列中已有数字(包含pre)的长度
            :param status: 解锁序列中已有数字(包含pre)的状态
            :return: 长度介于[m, n]的解锁序列数量
            """
            # 递归终止条件，长度已经取到最大值n了，不能再延长了
            if size == n:
                return 1
            total = 0 if size < m else 1
            for cur in range(1, 10):
                # 若数字cur还没被使用过。这个条件就已经包含了 pre != cur，因为pre肯定已经被使用过了
                if status & (1 << cur) == 0:
                    if cur not in graph[pre] or (status & (1 << graph[pre][cur])):
                        total += dfs(cur, size + 1, status | (1 << cur))
            return total

        # 从1出发的数量 * 4 + 从2出发的数量 * 4 + 从5出发的数量
        return dfs(1, 1, 1 << 1) * 4 + dfs(2, 1, 1 << 2) * 4 + dfs(5, 1, 1 << 5)


if __name__ == '__main__':
    print(Solution().numberOfPatterns(m=5, n=5))
