# -*- coding: UTF-8 -*-
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
