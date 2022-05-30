# -*- coding: UTF-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender2cnt = defaultdict(int)
        for msg, sender in zip(messages, senders):
            sender2cnt[sender] += msg.count(' ') + 1
        res = senders[0]
        for sender, cnt in sender2cnt.items():
            if cnt > sender2cnt[res] or (cnt == sender2cnt[res] and sender > res):
                res = sender
        return res


if __name__ == '__main__':
    print(Solution().largestWordCount(messages=["How is leetcode for everyone", "Leetcode is useful for practice"],
                                      senders=["Bob", "Charlie"]))
