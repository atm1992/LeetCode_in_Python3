# -*- coding: UTF-8 -*-
"""
title: 最后 K 个数的乘积
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
Implement the ProductOfNumbers class:
    ProductOfNumbers() Initializes the object with an empty stream.
    void add(int num) Appends the integer num to the stream.
    int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.


Example:
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
Output
[null,null,null,null,null,null,20,40,0,null,32]
Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32


Constraints:
0 <= num <= 100
1 <= k <= 4 * 10^4
At most 4 * 10^4 calls will be made to add and getProduct.
The product of the stream at any point in time will fit in a 32-bit integer.
"""


class ProductOfNumbers:
    """前缀积。记录最后一个0出现的下标"""

    def __init__(self):
        self.pre_product = [1]
        self.last_0 = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.last_0 = len(self.pre_product)
            num = 1
        self.pre_product.append(self.pre_product[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.pre_product)
        if n - k <= self.last_0:
            return 0
        return self.pre_product[n - 1] // self.pre_product[n - k - 1]


class ProductOfNumbers2:
    """前缀积。遇到0就清空前缀积数组，最后根据k与数组长度之间的大小关系来判断是否返回0"""

    def __init__(self):
        self.pre_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pre_product = [1]
        else:
            self.pre_product.append(self.pre_product[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.pre_product)
        if n <= k:
            return 0
        return self.pre_product[n - 1] // self.pre_product[n - k - 1]


if __name__ == '__main__':
    obj = ProductOfNumbers2()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    obj.add(8)
    print(obj.getProduct(2))
