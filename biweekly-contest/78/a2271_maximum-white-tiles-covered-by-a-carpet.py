# -*- coding: UTF-8 -*-
"""
title: 毯子覆盖的最多白色砖块数
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.
You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.
Return the maximum number of white tiles that can be covered by the carpet.


Example 1:
Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10.
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.

Example 2:
Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10.
It covers 2 white tiles, so we return 2.


Constraints:
1 <= tiles.length <= 5 * 10^4
tiles[i].length == 2
1 <= li <= ri <= 10^9
1 <= carpetLen <= 10^9
The tiles are non-overlapping.
"""
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        """贪心 + 滑动窗口"""
        tiles.sort()
        n = len(tiles)
        res = tmp_res = 0
        left = right = 0
        while right < n:
            left_boundary = tiles[left][0]
            right_boundary = left_boundary + carpetLen - 1
            if right_boundary >= tiles[right][1]:
                tmp_res += tiles[right][1] - tiles[right][0] + 1
                # 以防right加1后，等于n，退出了循环，此时没有更新res
                res = max(res, tmp_res)
                right += 1
            else:
                # 注意：这里先不要直接修改tmp_res。否则这里加一部分right，减去left后，上面再加一个完整的right，tmp_res就不对了
                tmp = tmp_res
                tmp += max(right_boundary - tiles[right][0] + 1, 0)
                if tmp == carpetLen:
                    return carpetLen
                res = max(res, tmp)
                tmp_res -= tiles[left][1] - tiles[left][0] + 1
                left += 1
        return res


if __name__ == '__main__':
    print(Solution().maximumWhiteTiles(tiles=[[10, 11], [1, 1]], carpetLen=2))
