# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树迭代器
实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
    BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
    boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
    int next()将指针向右移动，然后返回指针处的数字。
注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。


示例：
输入
inputs = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
inputs = [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
输出
[null, 3, 7, true, 9, true, 15, true, 20, false]
解释
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // 返回 3
bSTIterator.next();    // 返回 7
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 9
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 15
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 20
bSTIterator.hasNext(); // 返回 False


提示：
树中节点的数目在范围 [1, 10^5] 内
0 <= Node.val <= 10^6
最多调用 10^5 次 hasNext 和 next 操作

进阶：
你可以设计一个满足下述条件的解决方案吗？next() 和 hasNext() 操作均摊时间复杂度为 O(1) ，并使用 O(h) 内存。其中 h 是树的高度。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """使用栈来通过迭代的方式对二叉搜索树做中序遍历，无需预先计算出中序遍历的全部结果，只需实时维护当前栈的情况即可。
        初始化和hasNext()的时间复杂度为O(1)，next()的均摊时间复杂度为O(1)。空间复杂度为O(h)"""

    def __init__(self, root: TreeNode):
        self.cur_node = root
        self.stack = []

    def next(self) -> int:
        while self.cur_node:
            self.stack.append(self.cur_node)
            self.cur_node = self.cur_node.left
        # 可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。
        self.cur_node = self.stack.pop()
        res = self.cur_node.val
        self.cur_node = self.cur_node.right
        return res

    def hasNext(self) -> bool:
        return bool(self.cur_node) or bool(self.stack)


class BSTIterator2:
    """使用Morris遍历进行中序遍历。初始化和hasNext()的时间复杂度为O(1)，next()的均摊时间复杂度为O(1)。空间复杂度为O(1)"""

    def __init__(self, root: TreeNode):
        self.cur_node = root

    def next(self) -> int:
        # 可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。
        while self.cur_node.left:
            node = self.cur_node.left
            while node.right and node.right != self.cur_node:
                node = node.right
            if node.right == self.cur_node:
                node.right = None
                break
            else:
                node.right = self.cur_node
                self.cur_node = self.cur_node.left
        res = self.cur_node.val
        self.cur_node = self.cur_node.right
        return res

    def hasNext(self) -> bool:
        return bool(self.cur_node)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
