# -*- coding: UTF-8 -*-
"""
title: 监控二叉树
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.


Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.


Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val == 0
"""
from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        动态规划
        假设某棵树(子树)的所有节点都被监控，则称这棵树(子树)被覆盖。
        假设当前节点为node，其左孩子为left，其右孩子为right。存在两种覆盖情况：
        1、在当前节点node安装摄像头，则可监控到node、left、right。然后只需确保left的两棵子树以及right的两棵子树也能被覆盖；
        2、在当前节点node不安装摄像头，则除了覆盖node的两棵子树之外，还必须在left、right之一安装摄像头，才能保证node被监控到。
        根据上面的分析，定义3种状态：
        1、状态a: 在当前节点node安装摄像头的情况下，覆盖整棵子树所需的最小摄像头数量；
        2、状态b: 覆盖整棵子树所需的最小摄像头数量，无论是否在当前节点node安装摄像头；
        3、状态c: 在当前节点node不安装摄像头的情况下，覆盖当前节点node的两棵子树所需的最小摄像头数量，无论当前节点node能否被监控到。
        显然，题目所求最终结果为 当前节点node为root的状态b
        对于当前节点node而言，摄像头数量降序：状态a >= 状态b >= 状态c
        状态转移方程：
        node_a = left_c + right_c + 1
        node_b = min(node_a, left_a + right_b, left_b + right_a)
        node_c = min(node_a, left_b + right_b)
        对于node_c而言，要保证两棵子树被完全覆盖，要么在node处放置一个摄像头，则需要的摄像头数量为 node_a；
        要么在node处不放置摄像头，则此时两棵子树分别保证自己被覆盖，需要的摄像头数量为 left_b + right_b。
        当left、right均为叶节点时，left_b = right_b = 1，此时 node_a = 1 < 2 = left_b + right_b，即 left_b + right_b 不总是小于node_a
        边界条件：
        若当前节点node的左孩子left为空，则无法在left处安装摄像头，所以 left_a = float('inf'), left_b = left_c = 0
        因为树中的节点个数小于等于1000，所以摄像头数量肯定小于等于1000，因此可将left_a设置为1001
        """

        def dfs(node: TreeNode) -> Tuple[int, int, int]:
            if not node:
                return 1001, 0, 0
            left_a, left_b, left_c = dfs(node.left)
            right_a, right_b, right_c = dfs(node.right)
            node_a = left_c + right_c + 1
            node_b = min(node_a, left_a + right_b, left_b + right_a)
            node_c = min(node_a, left_b + right_b)
            return node_a, node_b, node_c

        return dfs(root)[1]

    def minCameraCover_2(self, root: TreeNode) -> int:
        """
        贪心。推荐此方法
        可定义3种状态：
        一、状态0：当前节点安装了摄像头；
        二、状态1：当前节点未安装摄像头，但能覆盖当前节点；
        三、状态2：当前节点未安装摄像头，且不能覆盖当前节点。
        分为3种情况来讨论状态转移(递推关系)：
        1、只要左右孩子中有一个未被覆盖(状态2)，哪怕另一个孩子安装了摄像头(状态0)，也必须在当前节点安装摄像头(状态0)；
        2、左右孩子均不存在未被覆盖的情况，且有一个孩子安装了摄像头(状态0)，则当前节点能被覆盖(状态1)；
        3、左右孩子均能被覆盖(状态1)，则当前节点上可以不安装摄像头，让当前节点的父节点去考虑(贪心)，所以此时当前节点的状态为不能覆盖(状态2)。特殊情况：当前节点为根节点，
        由于根节点不存在父节点，所以必须在根节点上加装一个摄像头。
        边界条件：
        空节点的状态：空节点上不能安装摄像头，所以状态值不能为0；空节点也不能是未被覆盖(状态2)，若未被覆盖，则意味着必须在其父节点安装摄像头，这与父节点为叶节点的情况不符；
        所以空节点的状态值应该为1
        """

        def dfs(node: TreeNode) -> int:
            nonlocal res
            if not node:
                return 1
            left_state = dfs(node.left)
            right_state = dfs(node.right)
            # 只要左右孩子中有一个未被覆盖(状态2)，哪怕另一个孩子安装了摄像头(状态0)，也必须在当前节点安装摄像头(状态0)
            if left_state == 2 or right_state == 2:
                res += 1
                return 0
            # 左右孩子均不存在未被覆盖的情况，且有一个孩子安装了摄像头(状态0)，则当前节点能被覆盖(状态1)
            elif left_state == 0 or right_state == 0:
                return 1
            # 左右孩子均能被覆盖(状态1)，则当前节点上可以不安装摄像头，让当前节点的父节点去考虑(贪心)，所以此时当前节点的状态为不能覆盖(状态2)
            else:
                return 2

        res = 0
        # 若根节点的状态为不能覆盖(状态2)，由于根节点不存在父节点，所以必须在根节点上加装一个摄像头
        if dfs(root) == 2:
            res += 1
        return res
