# -*- coding: UTF-8 -*-
"""
title: 执行操作后字典序最小的字符串
You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.
You can apply either of the following two operations any number of times and in any order on s:
    Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
    Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.
A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.


Example 1:
Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
Add:    "5121"
Rotate: "2151"
​​​​​​​Add:    "2050"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "2050".

Example 2:
Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
​​​​​​​Add:    "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "24".

Example 3:
Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".


Constraints:
2 <= s.length <= 100
s.length is even.
s consists of digits from 0 to 9 only.
1 <= a <= 9
1 <= b <= s.length - 1
"""
from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        枚举
        因为a <= 9，所以最多需要对所有奇数位加9次，加第10次时，就又循环到了初始值。因为 (x + a * 10) % 10 == x
        若b为偶数，则无论怎么向右旋转，加a操作始终都是针对的奇数位；若b为奇数，则既可对奇数位进行加a操作，也可对偶数位进行加a操作。
        无论b是奇数还是偶数，都最多只需向右旋转n-1次，旋转第n次时，就又回到了初始值。n = len(s)，对于任一下标i，(i - n * b) % n == i
        因此，若b为偶数，则最多存在 n * 10 种状态；若b为奇数，则最多存在 n * 10 * 10 种状态
        因此，可枚举所有的状态，找到最小的字符串
        """
        res = s
        n = len(s)
        s = list(s)
        # 向右旋转n次，最后那次旋转就是在处理初始值
        for _ in range(n):
            # 因为下一次旋转是对当前旋转产生的新字符串进行旋转，所以需要直接修改s
            s = s[-b:] + s[:-b]
            # 对数组s中的所有奇数位进行10次加a操作，最后那次操作就是在处理初始值
            for _ in range(10):
                for i in range(1, n, 2):
                    # 因为下一次加a是对当前加a产生的新字符串进行加a，所以需要直接修改数组s中的元素
                    s[i] = str((int(s[i]) + a) % 10)
                # 若b为奇数，则所有位都可以进行加a操作，在上面对数组s中的一半元素进行完加a操作后，会组成一个新字符串。
                # 对这个新字符串，可以通过若干次旋转将原处于偶数位的元素移动到奇数位，然后再进行10次加a操作，然后再转回到原来的偶数位
                # 先将偶数位的元素转到奇数位，最后再转回到原来的偶数位，这个过程无需使用代码实现，只要知道可以这么操作就行
                # 需要明白，当b为奇数时，在每次对奇数位进行加a操作后得到的新字符串，可以在经过若干次的旋转、10次加a操作、若干次的旋转后，
                # 对该新字符串的所有偶数位进行加a操作，扩展出10种新的状态。所以是 n * 10 * 10 种状态
                if b & 1:
                    for _ in range(10):
                        for i in range(0, n, 2):
                            s[i] = str((int(s[i]) + a) % 10)
                        t = ''.join(s)
                        if t < res:
                            res = t
                else:
                    t = ''.join(s)
                    if t < res:
                        res = t
        return res

    def findLexSmallestString_2(self, s: str, a: int, b: int) -> str:
        """BFS 暴力搜索所有可能的状态"""
        queue = deque([s])
        visited = {s}
        res = s
        while queue:
            cur = queue.popleft()
            if cur < res:
                res = cur
            nxt1 = ''.join(str((int(ch) + a) % 10) if i & 1 else ch for i, ch in enumerate(cur))
            nxt2 = cur[-b:] + cur[:-b]
            for nxt in [nxt1, nxt2]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return res


if __name__ == '__main__':
    print(Solution().findLexSmallestString_2(s="74", a=5, b=1))
