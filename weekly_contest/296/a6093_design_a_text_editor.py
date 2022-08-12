# -*- coding: UTF-8 -*-
"""
title: 设计一个文本编辑器
Design a text editor with a cursor that can do the following:
    Add text to where the cursor is.
    Delete text from where the cursor is (simulating the backspace key).
    Move the cursor either left or right.
When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.
Implement the TextEditor class:
    TextEditor() Initializes the object with empty text.
    void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
    int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
    string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
    string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.


Example 1:
Input
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
Output
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]
Explanation
TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
                          // The current text is "leet|".
                          // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|".
textEditor.cursorRight(3); // return "etpractice"
                           // The current text is "leetpractice|".
                           // The cursor cannot be moved beyond the actual text and thus did not move.
                           // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
                          // The current text is "leet|practice".
                          // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
                           // The current text is "|practice".
                           // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
                          // The current text is "|practice".
                          // The cursor cannot be moved beyond the actual text and thus did not move.
                          // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
                           // The current text is "practi|ce".
                           // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.


Constraints:
1 <= text.length, k <= 40
text consists of lowercase English letters.
At most 2 * 10^4 calls in total will be made to addText, deleteText, cursorLeft and cursorRight.
"""


class Node:
    # 若不加__slots__，则底层需要使用哈希表来动态维护对象的属性；
    # 加上 __slots__ 之后，相当于每个 Node 对象的大小变为固定，不再需要使用哈希表去维护属性，适用于对象初始化后不再新增属性的场景。
    # 加上 __slots__ ，可以提升执行速度
    __slots__ = ('pre', 'nxt', 'ch')

    def __init__(self, ch: str = ''):
        self.ch = ch
        self.pre = None
        self.nxt = None

    def insert(self, node: 'Node') -> 'Node':
        """在当前节点self之后插入新节点node，然后返回新节点node"""
        node.pre = self
        node.nxt = self.nxt
        node.pre.nxt = node
        node.nxt.pre = node
        return node

    def remove(self) -> 'Node':
        """移除当前节点self，然后返回self的前驱节点。循环双向链表，无需判空，因为至少会存在self.dummy_head"""
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        return self.pre


class TextEditor:
    """循环双向链表模拟"""

    def __init__(self):
        # 哨兵节点。表示光标位于文本最左侧的情况，此时光标左侧没有字符
        self.dummy_head = Node()
        self.dummy_head.pre = self.dummy_head
        self.dummy_head.nxt = self.dummy_head
        # 当前节点中保存着光标左侧的最后一个字符
        self.cur_node = self.dummy_head

    def addText(self, text: str) -> None:
        for ch in text:
            self.cur_node = self.cur_node.insert(Node(ch))

    def deleteText(self, k: int) -> int:
        res = 0
        while self.cur_node != self.dummy_head and res < k:
            res += 1
            self.cur_node = self.cur_node.remove()
        return res

    def getLeftText(self) -> str:
        res = []
        cnt = 0
        # 注意：这里不能修改self.cur_node
        cur_node = self.cur_node
        while cur_node != self.dummy_head and cnt < 10:
            cnt += 1
            res.append(cur_node.ch)
            cur_node = cur_node.pre
        return ''.join(res[::-1])

    def cursorLeft(self, k: int) -> str:
        while self.cur_node != self.dummy_head and k > 0:
            k -= 1
            self.cur_node = self.cur_node.pre
        return self.getLeftText()

    def cursorRight(self, k: int) -> str:
        while self.cur_node.nxt != self.dummy_head and k > 0:
            k -= 1
            self.cur_node = self.cur_node.nxt
        return self.getLeftText()


class TextEditor2:
    """
    对顶栈。执行速度远快于上个方法
    两个栈的栈顶对栈顶，光标的左右移动就相当于两个栈来回倒。对于插入和删除操作，就相当于在左边那个栈的栈顶出入栈。
    """

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        cnt = min(len(self.left), k)
        for _ in range(cnt):
            self.left.pop()
        return cnt

    def getLeftText(self) -> str:
        return ''.join(self.left[-10:])

    def cursorLeft(self, k: int) -> str:
        cnt = min(len(self.left), k)
        for _ in range(cnt):
            self.right.append(self.left.pop())
        return self.getLeftText()

    def cursorRight(self, k: int) -> str:
        cnt = min(len(self.right), k)
        for _ in range(cnt):
            self.left.append(self.right.pop())
        return self.getLeftText()

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
