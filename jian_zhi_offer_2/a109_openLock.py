# -*- coding: UTF-8 -*-
"""
title: 开密码锁
一个密码锁由 4 个环形拨轮组成，每个拨轮都有 10 个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，请给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。


示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，因为当拨动到 "0102" 时这个锁就会被锁定。

示例 2:
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。

示例 3:
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。

示例 4:
输入: deadends = ["0000"], target = "8888"
输出：-1


提示：
1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target 不在 deadends 之中
target 和 deadends[i] 仅由若干位数字组成
"""
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """BFS"""
        start = '0000'
        if start == target:
            return 0
        dead_set = set(deadends)
        if start in dead_set:
            return -1
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            item, step = queue.popleft()
            for i in range(4):
                ch1 = str((int(item[i]) + 1) % 10)
                # 在Python中，-1 % 10 == 9
                ch2 = str((int(item[i]) - 1) % 10)
                for ch in [ch1, ch2]:
                    next_item = item[:i] + ch + item[i + 1:]
                    if next_item not in dead_set and next_item not in visited:
                        if next_item == target:
                            return step + 1
                        queue.append((next_item, step + 1))
                        visited.add(next_item)
        return -1

    def openLock_2(self, deadends: List[str], target: str) -> int:
        """双向BFS"""
        start = '0000'
        if start == target:
            return 0
        dead_set = set(deadends)
        if start in dead_set:
            return -1
        forward_queue, backward_queue = deque([start]), deque([target])
        forward_visited, backward_visited = {start: 0}, {target: 0}
        while forward_queue:
            if len(forward_queue) > len(backward_queue):
                forward_queue, backward_queue = backward_queue, forward_queue
                forward_visited, backward_visited = backward_visited, forward_visited
            for _ in range(len(forward_queue)):
                item = forward_queue.popleft()
                for i in range(4):
                    ch1 = str((int(item[i]) + 1) % 10)
                    # 在Python中，-1 % 10 == 9
                    ch2 = str((int(item[i]) - 1) % 10)
                    for ch in [ch1, ch2]:
                        next_item = item[:i] + ch + item[i + 1:]
                        if next_item not in dead_set and next_item not in forward_visited:
                            if next_item in backward_visited:
                                # forward_visited、backward_visited 中的层级均从0开始
                                return forward_visited[item] + backward_visited[next_item] + 1
                            forward_queue.append(next_item)
                            forward_visited[next_item] = forward_visited[item] + 1
        return -1


if __name__ == '__main__':
    print(Solution().openLock_2(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
