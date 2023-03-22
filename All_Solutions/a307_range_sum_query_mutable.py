# -*- coding: UTF-8 -*-
"""
title: 区域和检索 - 数组可修改
Given an integer array nums, handle multiple queries of the following types:
    Update the value of an element in nums.
    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
    NumArray(int[] nums) Initializes the object with the integer array nums.
    void update(int index, int val) Updates the value of nums[index] to be val.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]
Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 10^4 calls will be made to update and sumRange.

解题思路：
若输入数组nums是不可变的：
    方法一、可在构造函数中初始化一个前缀和数组，时间复杂度为O(n)；之后每次调用sumRange获取区间和的时间复杂度为O(1)


若输入数组nums是可变的：
    方法一：可参考上述方法，在构造函数中初始化一个前缀和数组，时间复杂度为O(n)；根据update 与 sumRange的调用次数对比，选择在哪个方法中更新前缀和数组，
    若update调用较多，而sumRange调用较少，则可将更新前缀和数组这个操作放在sumRange方法中，此时update保持O(1)，sumRange为O(n)。
    如果update / sumRange的调用次数都很多，均为m，则总体时间复杂度为O(mn)，因此本题不适用此方法


    方法二：分块处理。可对上述方法进行折中，如果update / sumRange的调用次数均为m。可以对原数组nums分块求前缀和，
    那样update val后，也只需更新相应那块的前缀和，其它块的前缀和不受影响。
    当块size取值为int(n ** 0.5)时，可将sumRange的时间复杂度降为O(sqrt(n))，而update保持O(1)


    方法三：树状数组。树状数组的核心思想就是将一个前缀和划分成多个子序列的和，根据索引的二进制表示来划分。
    例如：求13的前缀和，13 的二进制表示为 1101，2^3 + 2^2 + 2^0 = 8 + 4 + 1 = range(1, 8) + range(9, 12) + range(13, 13)
    range(i，j) 表示闭区间 [i, j] 的区间和bit[j]，根据 j 可计算出 i，i = j - lowbit(j) + 1，其中，lowbit(j) 表示j的二进制表示中最低一个1所代表的数值，
    如果j的二进制表示中只有一个1，则lowbit(j)就是j本身，lowbit(8) = 8，lowbit(12) = 4，lowbit(13) = 1
    综上，pre_sum(13) = range(1, 8) + range(9, 12) + range(13, 13) = bit[8] + bit[12] + bit[13] = bit[13] + bit[12] + bit[8]
    res = 0
    i = 13
    res += bit[13]
    i = i - lowbit(i) = 13 - lowbit(13) = 13 - 1 = 12
    res += bit[12]
    i = i - lowbit(i) = 12 - lowbit(12) = 12 - 4 = 8
    res += bit[8]
    i = i - lowbit(i) = 8 - lowbit(8) = 8 - 8 = 0           # i 需要大于0，所以循环终止

    更新元素值update，跟上面计算前缀和是个逆向过程，假设需要将下标i为8的元素值更新为val，则除了需要更新nums[8] 和 bit[9]，还需更新bit[10]、bit[12] ……
    # 注意：原数组nums中的下标i从0开始，而树状数组中的下标i是从1开始，树状数组中的下标0并不使用，存储默认值0。
    i = 8
    n = len(nums) = 14
    diff = val - nums[8]
    nums[8] = val
    i = i + 1 = 9           # 树状数组中的下标i是从1开始
    bit[9] += diff
    i = i + lowbit(i) = 9 + lowbit(9) = 9 + 1 = 10
    bit[10] += diff
    i = i + lowbit(i) = 10 + lowbit(10) = 10 + 2 = 12
    bit[12] += diff
    i = i + lowbit(i) = 12 + lowbit(12) = 12 + 4 = 16        # i 需要小于等于n=14，所以循环终止

    初始化(建树)             # 注意：树状数组并不是一棵树，本质上还是一个数组
    有两种方法：
    一、先初始化一个元素值均为0、长度为n+1的数组，然后调用n次update。此时初始化的时间复杂度为O(nlogn)，因为单次update的时间复杂度为O(logn)
    二、先将bit数组初始化为 [0] + nums，遍历 [1, n]中的每个i，更新bit[j] = bit[j] + bit[i]，其中 j = i + lowbit(i)。注意：每次更新的都是bit[j]，而不是bit[i]


    方法四：线段树(Segment Tree)。树状数组是利用索引的二进制表示来划分子序列，而线段树是不断进行二分来划分子序列。不像树状数组，线段树的确是一棵二叉树。不过使用的还是数组的顺序存储
    构建线段树也有两种方法：
    一、采用自顶向下不断递归直到叶结点的建树方式，这就是普通的线段树，需要不断地递归压栈；
    二、采用自底向上迭代的建树方式，这就是常用的zkw线段树（出自张昆玮的论文《统计的力量》，zkw即其名字缩写）
    最坏情况下，需要使用大小约为4*n的空间来构建线段树，例如：n=17，则在后面补15个0，将原数组nums扩充为32，然后再取2*n。
    其实用2*n的空间来构建线段树也一样是可以的，本文将以迭代的方式、使用2*n的空间来构建线段树！
    方法一代码：
    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    方法二代码：
    self.st = [0]*n + nums          # 线段树ST长度为2n。其实真正使用的是后面2n-1个元素，可理解为线段树的下标i也是从1开始
    for i in range(n-1, 0, -1):     # [1, n-1] 倒序添加子节点之和，st[0] 是无用的，真正使用的是st[1] ~ st[2n-1]
        # ST[2i]、ST[2i+1]分别为ST[i]的左/右子节点
        self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
"""
import math
from typing import List


class NumArray:
    """分块处理。sumRange的时间复杂度为O(sqrt(n))，update的时间复杂度为O(1)"""

    def __init__(self, nums: List[int]):
        n = len(nums)
        size = int(n ** 0.5)
        # 表示将原数组nums分为多少块，最后一块可能不足size个
        pre_sum = [0] * math.ceil(n / size)
        for idx, num in enumerate(nums):
            pre_sum[idx // size] += num
        self.nums = nums
        self.pre_sum = pre_sum
        self.size = size

    def update(self, index: int, val: int) -> None:
        self.pre_sum[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        m = self.size
        # 分别计算left、right所在的分块数
        b1, b2 = left // m, right // m
        # 若left、right同属一个分块，则说明数据量不大，直接求和返回就行
        if b1 == b2:
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:m * (b1 + 1)]) + sum(self.pre_sum[b1 + 1:b2]) + sum(self.nums[m * b2:right + 1])


class NumArray2:
    """树状数组。sumRange 以及 update的时间复杂度均为O(logn)"""

    def low_bit(self, idx: int) -> int:
        # 负数的补码为其绝对值的原码按位取反(符号位除外)，然后加1
        return idx & -idx

    def __init__(self, nums: List[int]):
        # 这里之所以选择存储原数组nums，是为了在update时能够方便获取self.nums[index]，
        # 其实self.nums[index]也可通过self.sumRange(index, index)来获取，但这样的话，时间复杂度就更高了
        self.nums = nums
        self.bit = [0] + nums
        self.bit_size = len(self.bit)
        # 这种方式构造的BIT时间复杂度为O(n)。而不是连续调用n次update
        for i in range(1, self.bit_size):
            j = i + self.low_bit(i)
            if j < self.bit_size:
                self.bit[j] += self.bit[i]

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        # 既然选择了存储self.nums，那就要记得更新self.nums[index]，避免下次再通过self.nums获取相同index的值时，不能获取到更新后的值
        self.nums[index] = val
        # 树状数组中的下标i是从1开始
        index += 1
        while index < self.bit_size:
            self.bit[index] += delta
            index += self.low_bit(index)

    def pre_sum(self, idx: int) -> int:
        """这里是计算bit数组的前缀和，idx范围为[1, self.bit_size - 1]"""
        res = 0
        while idx > 0:
            res += self.bit[idx]
            # 等价于 idx &= idx - 1
            idx -= self.low_bit(idx)
        return res

    def sumRange(self, left: int, right: int) -> int:
        # 树状数组bit中的下标i是从1开始
        left, right = left + 1, right + 1
        # bit数组的前缀和right 减去 bit数组的前缀和left-1
        return self.pre_sum(right) - self.pre_sum(left - 1)


class NumArray3:
    """线段树。sumRange 以及 update的时间复杂度均为O(logn)"""

    def __init__(self, nums: List[int]):
        # 线段树不像树状数组那样，需要考虑存储原数组nums，因为线段树后面的那n个元素就是原始的数组元素
        n = len(nums)
        # 线段树ST的长度为2n。注意：此时的线段树并不是一颗完全二叉树，虽然原数组nums中的所有元素均为叶节点，也不存在度为1的节点，
        # 但是所有的叶节点并非都在最底层。以 n = 3 为例验证可知，忽略st[0]，将st[1]视作根节点，可知st[3]作为叶节点，却在倒数第二层。
        st = [0] * n + nums
        # st[0]是无用的，线段树的下标也是从1开始
        for i in range(n - 1, 0, -1):
            st[i] = st[2 * i] + st[2 * i + 1]
        self.n = n
        self.st = st

    def update(self, index: int, val: int) -> None:
        # 将原数组nums下标转换为线段树ST的下标
        idx = index + self.n
        delta = val - self.st[idx]
        # 只需向上更新到st[1]
        while idx > 0:
            self.st[idx] += delta
            idx //= 2

    def sumRange(self, left: int, right: int) -> int:
        # 将原数组nums下标转换为线段树ST的下标
        i, j = left + self.n, right + self.n
        res = 0
        while i <= j:
            # 若st[i]是右子节点，则先向右走一步，否则直接向上走一步
            # 注意：i 是左边界
            if i & 1:
                res += self.st[i]
                i += 1
            # 若st[j]是左子节点，则先向左走一步，否则直接向上走一步
            # 注意：j 是右边界
            if not j & 1:
                res += self.st[j]
                j -= 1
            # i, j 均向上走一步
            i, j = i >> 1, j >> 1
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
