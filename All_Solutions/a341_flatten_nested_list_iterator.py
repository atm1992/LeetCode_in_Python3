# -*- coding: UTF-8 -*-
"""
title: 扁平化嵌套列表迭代器
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
Implement the NestedIterator class:
    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:
    initialize iterator with nestedList
    res = []
    while iterator.hasNext()
        append iterator.next() to the end of res
    return res
If res matches the expected flattened list, then your code will be judged as correct.


Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].
"""

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    """
    Python可使用生成器
    注意：迭代器的设计不能在初始化的时候，就事先把所有元素都存储到列表中
    """
    def __init__(self, nestedList: [NestedInteger]):
        def get_generator(nestedList: [NestedInteger]):
            for nest in nestedList:
                if nest.isInteger():
                    yield nest.getInteger()
                else:
                    yield from get_generator(nest.getList())
        self.gen = get_generator(nestedList)
        self.cache = next(self.gen, None)

    def next(self) -> int:
        res = self.cache
        self.cache = next(self.gen, None)
        return res

    def hasNext(self) -> bool:
        return self.cache is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
