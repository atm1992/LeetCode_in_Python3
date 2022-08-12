# -*- coding: UTF-8 -*-
"""
title: 账户合并
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """哈希表 + 并查集"""
        # 给每个email地址分配一个唯一的id
        email2id, email2name = {}, {}
        cnt = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email2id:
                    email2id[email] = cnt
                    cnt += 1
                    email2name[email] = name

        parent = list(range(cnt))

        def find(i: int) -> int:
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> None:
            parent[find(i)] = find(j)

        for account in accounts:
            # 2 <= accounts[i].length
            parent_id = email2id[account[1]]
            for email in account[2:]:
                union(email2id[email], parent_id)

        parent_id2emails = defaultdict(list)
        # 这里的变量名用i，而不是id，是因为id是一个Python内建的方法名
        for email, i in email2id.items():
            parent_id2emails[find(i)].append(email)

        res = []
        for emails in parent_id2emails.values():
            name = email2name[emails[0]]
            res.append([name] + sorted(emails))
        return res


if __name__ == '__main__':
    print(Solution().accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                             ["John", "johnsmith@mail.com", "john00@mail.com"],
                                             ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
