# -*- coding: UTF-8 -*-
"""
title: 根据身高重建队列
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).


Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]


Constraints:
1 <= people.length <= 2000
0 <= hi <= 10^6
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        根据身高从低到高考虑。
        将返回结果初始化为一个长度为n的空队列，优先安排矮的，根据相应的k值来决定放到哪个空的位置，如果当前people的k为2，也就意味着从左往右数的过程中，
        需要预留出两个空位置，然后将当前people放到第2 + 1个空位置上，因为后面放的people身高都会比他高。之后安排其它的高的人时，前面安排的所有人都比他矮，
        即 前面的所有人都对他的k没有影响。
        以上没有考虑身高相同的情况，假设存在如下两个people：(3, 1)、(3, 3)，此时应该优先安排(3, 3)，因为(3, 3)毫无疑问会排在(3, 1)的后面，
        最终结果中，排在后面的，对排在前面的不会有任何影响。假设先安排了(3, 1)，再去安排(3, 3)，此时会需要预留3个空位置去放比他高或者一样高的人，
        然而加上前面放的(3, 1)，会导致(3, 3)前面有4个比他高或者一样高的人，不符合要求！
        """
        # 先按h升序，h相同的情况下，再按k降序
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        res = [[] for _ in range(n)]
        for item in people:
            # 查找第k + 1个空位置，前面预留k个空位置
            spaces = item[1] + 1
            for i in range(n):
                if not res[i]:
                    spaces -= 1
                    if spaces == 0:
                        res[i] = item
                        break
        return res

    def reconstructQueue_2(self, people: List[List[int]]) -> List[List[int]]:
        """
        根据身高从高到低考虑。执行速度比上个方法快。
        反向思考，优先安排高的，根据相应的k值来决定插入到谁的后面，若当前people的k为2，也就意味着从左往右数的过程中，插入到第2个人的后面。
        之后插入的人，不会对他有影响，因为都比他矮。
        对于身高相同的情况，假设存在如下两个people：(3, 1)、(3, 3)，此时应该优先安排(3, 1)，因为(3, 1)毫无疑问会排在(3, 3)的前面。
        安排(3, 3)的时候，需要把(3, 1)算入在他的k当中。
        """
        # 先按h降序，h相同的情况下，再按k升序
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for item in people:
            # 注意：元素下标是从0开始，所以这里是item[1]，而不是item[1] + 1
            res.insert(item[1], item)
        return res


if __name__ == '__main__':
    print(Solution().reconstructQueue_2([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
