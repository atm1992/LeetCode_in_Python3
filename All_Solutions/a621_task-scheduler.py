# -*- coding: UTF-8 -*-
"""
title: 任务调度器
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.


Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:
1 <= task.length <= 10^4
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """模拟。不断选择不在冷却中并且剩余执行次数最多的那个任务"""
        if n == 0:
            return len(tasks)
        # heapq 默认是最小堆，升序。元组中的第一个元素表示下一次允许执行的时间，所有任务的下一次执行时间均为初始值1，time从1开始计算。
        # 元组中的第二个元素表示该任务剩余执行的次数。优先选择执行时间最近的(升序)，执行时间相同的情况下，再优先选择剩余执行次数最多的(降序)
        nextValid_restCnt = [(1, -v) for k, v in Counter(tasks).items()]
        # 因为tasks用大写字母表示，所以优先队列的长度不超过26
        heapq.heapify(nextValid_restCnt)
        res = 0
        while nextValid_restCnt:
            # 每次分配任务之前，都需要在上一次结果的基础上加1，来表示当前时间
            res += 1
            nextValid, restCnt = heapq.heappop(nextValid_restCnt)
            # 找到所有nextValid小于当前时间res的任务，取这些任务当中，剩余执行次数最多的那个
            if nextValid < res:
                tmp = [(nextValid, restCnt)]
                while nextValid_restCnt:
                    next_valid_time = nextValid_restCnt[0][0]
                    if next_valid_time <= res:
                        tmp.append(heapq.heappop(nextValid_restCnt))
                    # 第一个等于，会先进入上面的if，然后进入这个if
                    if next_valid_time >= res:
                        break
                the_idx = 0
                for i in range(1, len(tmp)):
                    # restCnt是一个负数
                    if tmp[i][1] < restCnt:
                        the_idx = i
                        nextValid, restCnt = tmp[i]
                tmp.pop(the_idx)
                for v, c in tmp:
                    heapq.heappush(nextValid_restCnt, (v, c))
            res = max(res, nextValid)
            nextValid += n + 1
            # restCnt是一个负数，当它从负数一直加1，加到0的时候，就无需再进入优先队列了
            restCnt += 1
            if restCnt < 0:
                heapq.heappush(nextValid_restCnt, (nextValid, restCnt))
        return res

    def leastInterval_2(self, tasks: List[str], n: int) -> int:
        """数学。假设所有任务中的最大执行次数为max_exec, 执行次数为max_exec的任务有max_cnt个，因此，其余任务的执行次数小于max_exec。
        所有任务最终会按时间线排成一条序列，假设将这条序列分割成长度为 n + 1 的子序列，每一行最多有n+1个元素
        以 tasks = ["A","A","A","A","B","B","B","B","C","C","D","D","E"], n = 3 为例，变成如下二维矩阵：
        "A","B","C","D"
        "A","B","C","E"   ————> "A","B","C","D","A","B","C","E","A","B","D"," ","A","B"
        "A","B","D"," "
        "A","B"
        该二维矩阵最多有max_exec行，每行最多有n+1个元素，总的单元格个数为 (max_exec - 1) * (n+1) + max_cnt
        对所有任务根据执行次数降序排列，先安排执行次数最多的那些任务，再安排执行次数次多的，以此类推 ……
        排列规则为：先用执行次数为max_cnt的任务填充左侧的列，然后用执行次数次多的任务填充接下来的列，不过最多只允许向下填充至倒数第二行，
        因为这些任务的执行次数最多为max_exec - 1，从第一行到倒数第二行刚好是max_exec - 1个位置，同一任务要么在同一列，要么在相邻的两列(例如上面的"D")，
        同一列相邻行的元素之间间隔为n，相邻两列相邻行的元素之间间隔为n-1。但由于这部分任务的执行次数最多为max_exec - 1，所以它们不可能位于相邻两列的相邻行，
        相邻两列的同一任务至少会间隔一行，也就是说，这些任务的间隔至少为 n + 1 + (n-1) = 2n >= n
        上述计算公式适用于n+1列足够填充所有元素的情况，但如果n+1列无法填充完所有元素，我们可以按上述规则继续填充剩余元素，使得列数超过n+1，
        此时同一列的元素之间间隔将会大于n，因此将不再需要填充空闲来使同一任务之间的间隔至少为n，因此可以去掉所有的空闲，完全用任务来填充，
        此时，总的单元格个数就是任务总数。
        最终结果就是 (max_exec - 1) * (n+1) + max_cnt 与 任务总数 之间取较大值！
        注意：因为(max_exec - 1) * (n+1) + max_cnt最多只按n+1列计算，当列数超过n+1时(没有空闲)，它的计算结果肯定会小于任务总数，取较大值时，就会取任务总数。
        """
        task2cnt = Counter(tasks)
        max_exec = max(task2cnt.values())
        max_cnt = 0
        for v in task2cnt.values():
            if v == max_exec:
                max_cnt += 1
        return max((max_exec - 1) * (n + 1) + max_cnt, len(tasks))


if __name__ == '__main__':
    print(Solution().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
