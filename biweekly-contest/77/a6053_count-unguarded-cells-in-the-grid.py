# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # a - 未被保护，b - 被保护
        graph = [['a'] * n for _ in range(m)]
        for i, j in guards:
            graph[i][j] = 'g'
        for i, j in walls:
            graph[i][j] = 'w'
        for i, j in guards:
            for k in range(i - 1, -1, -1):
                if graph[k][j] in ['g', 'w']:
                    break
                graph[k][j] = 'b'
            for k in range(i + 1, m):
                if graph[k][j] in ['g', 'w']:
                    break
                graph[k][j] = 'b'
            for k in range(j - 1, -1, -1):
                if graph[i][k] in ['g', 'w']:
                    break
                graph[i][k] = 'b'
            for k in range(j + 1, n):
                if graph[i][k] in ['g', 'w']:
                    break
                graph[i][k] = 'b'
        res = 0
        for i in range(m):
            res += graph[i].count('a')
        return res


if __name__ == '__main__':
    print(Solution().countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]))
