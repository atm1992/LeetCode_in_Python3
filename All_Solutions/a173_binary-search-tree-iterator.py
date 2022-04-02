# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树迭代器
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.


Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]
Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False


Constraints:
The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^6
At most 10^5 calls will be made to hasNext, and next.

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """扁平化。直接对二叉搜索树做一次中序遍历，将遍历结果存储到一个数组中，然后使用结果数组来实现迭代器。
    初始化的时间复杂度为O(n)，next() 和 hasNext()的时间复杂度为O(1)。空间复杂度为O(n)"""

    def __init__(self, root: TreeNode):
        self.arr = []
        self.idx = 0
        self.inorder_traversal(root)

    def inorder_traversal(self, node: TreeNode):
        if not node:
            return
        self.inorder_traversal(node.left)
        self.arr.append(node.val)
        self.inorder_traversal(node.right)

    def next(self) -> int:
        res = self.arr[self.idx]
        self.idx += 1
        return res

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)


class BSTIterator2:
    """使用栈来通过迭代的方式对二叉搜索树做中序遍历，无需预先计算出中序遍历的全部结果，只需实时维护当前栈的情况即可。
    初始化和hasNext()的时间复杂度为O(1)，next()的均摊时间复杂度为O(1)。空间复杂度为O(h)"""

    def __init__(self, root: TreeNode):
        self.cur_node = root
        self.stack = []

    def next(self) -> int:
        while self.cur_node:
            self.stack.append(self.cur_node)
            self.cur_node = self.cur_node.left
        self.cur_node = self.stack.pop()
        res = self.cur_node.val
        self.cur_node = self.cur_node.right
        return res

    def hasNext(self) -> bool:
        return bool(self.cur_node) or bool(self.stack)


class BSTIterator3:
    """使用Morris遍历进行中序遍历。初始化和hasNext()的时间复杂度为O(1)，next()的均摊时间复杂度为O(1)。空间复杂度为O(1)"""

    def __init__(self, root: TreeNode):
        self.cur_node = root

    def next(self) -> int:
        # 题目可以保证 next() calls will always be valid.
        while self.cur_node.left:
            node = self.cur_node.left
            while node.right and node.right != self.cur_node:
                node = node.right
            if node.right:
                node.right = None
                break
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
