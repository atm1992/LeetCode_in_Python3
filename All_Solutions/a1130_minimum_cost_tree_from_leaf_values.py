# -*- coding: UTF-8 -*-
"""
title: 叶值的最小代价生成树
Given an array arr of positive integers, consider all binary trees such that:
    Each node has either 0 or 2 children;
    The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
    The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.
A node is a leaf if and only if it has zero children.


Example 1:
Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

Example 2:
Input: arr = [4,11]
Output: 44


Constraints:
2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).
"""
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        贪心 + 单调递减栈
        要想生成树的代价最小，那么应尽量将较小的值作为更底层的叶节点，而较大的值作为更上层的叶节点，越大的值越后面使用。类似于 哈夫曼树
        因为给定数组arr是中序遍历的叶节点数组，所以各个叶节点之间的左右顺序是确定的，可以调整的是各个叶节点的所在高度，让越大的叶节点越靠近根节点。
        通过维护一个单调递减栈来逐步查找当前的极小值(栈顶节点)，找到极小值(栈顶节点)后，比较下其左侧叶节点(栈顶节点的下一个节点)与右侧叶节点(当前节点)的大小，
        将较小者与极小值(栈顶节点)进行合并，然后pop极小值(栈顶节点)，因为其左侧叶节点与右侧叶节点肯定都大于等于极小值(栈顶节点)，而每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积，
        所以此极小值之后不会再被使用了
        """
        res = 0
        # arr[i] <= 15。初始时放入一个哨兵节点
        stack = [16]
        for num in arr:
            # 哨兵节点16肯定会一直存在，所以stack不可能为空
            while stack[-1] <= num:
                res += stack.pop() * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


if __name__ == '__main__':
    print(Solution().mctFromLeafValues(arr=[6, 2, 4]))
