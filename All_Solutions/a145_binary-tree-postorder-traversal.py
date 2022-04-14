# -*- coding: UTF-8 -*-
"""
title：二叉树的后序遍历
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res

    def postorderTraversal_2(self, root: TreeNode) -> List[int]:
        """后序遍历的迭代版本。若类似于前序遍历直接写，会有些麻烦，因为这里需要判断节点的访问状态，根节点需要最后出栈。
        转换思路，将后序(左->右->根)看作是(根->右->左)的逆序。这里本质上还是前序遍历，并不是真正的后序遍历，因此不建议这种写法"""
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            # 先打印根节点
            res.append(node.val)
            # 左孩子先入栈，后出栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈，因此会先出栈，也就是会先打印右孩子，然后再打印左孩子
            if node.right:
                stack.append(node.right)
        res.reverse()
        # 注意：不能直接return res.reverse()，因为reverse()方法没有返回值。
        # 逆序也可以使用 return res[::-1]
        return res

    def postorderTraversal_3(self, root: TreeNode) -> List[int]:
        """迭代。不用逆序"""
        res = []
        stack = []
        pre_node = None
        cur_node = root
        while cur_node or stack:
            # 若存在左孩子，则一路向左。否则向右走一步，接着继续遍历左，直到既没有左孩子，也没有右孩子。
            # 此时才开始加入res，使用变量pre_node来记录上一次加入到res的节点，从而避免重复加入，进入死循环。
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            if not cur_node.right or cur_node.right == pre_node:
                res.append(cur_node.val)
                # 使用pre_node来记录上一次加入到res的节点，从而避免重复加入，进入死循环。想象一条只有右节点的边，从下往上逐个将节点加入res
                pre_node = cur_node
                cur_node = None
            else:
                # 存在右孩子节点，且该右孩子节点不等于pre_node，则先将前面pop出来的节点加回stack，然后向右走一步
                stack.append(cur_node)
                cur_node = cur_node.right
        return res
