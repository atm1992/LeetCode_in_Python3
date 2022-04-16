# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        """枚举中间两个点。假设最终的4个点为：a - x - y - b。枚举edges中的每条边(x - y)，然后在x的相邻点中找到分数最大且不等于y和b的点，
        同理，在y的相邻点中找到分数最大且不等于a和x的点。因此对于每个点，其实只需保留分数最大的3个相邻点即可"""
        n = len(scores)
        nodes = [[] for _ in range(n)]
        for x, y in edges:
            nodes[x].append(y)
            nodes[y].append(x)
        for i in range(n):
            nodes[i].sort(key=lambda x: -scores[x])

        res = -1
        for x, y in edges:
            for a in nodes[x][:3]:
                for b in nodes[y][:3]:
                    if len({a, x, y, b}) == 4:
                        # 去掉这里的print，加上会超时
                        # print([a, x, y, b])
                        res = max(res, scores[a] + scores[x] + scores[y] + scores[b])

        return res


if __name__ == '__main__':
    print(Solution().maximumScore([14, 12, 10, 8, 1, 2, 3, 1],
                                  [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 1], [2, 1]]))
