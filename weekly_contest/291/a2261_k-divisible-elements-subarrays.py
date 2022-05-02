# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """暴力破解 + set去重"""
        res = set()
        n = len(nums)
        for start in range(n):
            cnt = 0
            for end in range(start, n):
                if nums[end] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                res.add(tuple(nums[start: end + 1]))
        return len(res)

    def countDistinct_2(self, nums: List[int], k: int, p: int) -> int:
        """字典树。每产生一个不同的子数组，必将会在字典树中插入一个新节点。最终答案 = 字典树中新插入的节点数量"""
        # 根节点初始时，为一个空dict
        trie = [{}]

        def insert_node() -> int:
            # 新加一个空节点
            trie.append({})
            # 返回新加节点在trie数组中的下标
            return len(trie) - 1

        for i in range(len(nums)):
            cnt = 0
            # 每次都是从根节点开始找
            node_idx = 0
            for num in nums[i:]:
                if num % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                if num not in trie[node_idx]:
                    trie[node_idx][num] = insert_node()
                node_idx = trie[node_idx][num]
        # 需要除去根节点
        return len(trie) - 1


if __name__ == '__main__':
    print(Solution().countDistinct_2(nums=[2, 3, 3, 2, 2], k=2, p=2))
