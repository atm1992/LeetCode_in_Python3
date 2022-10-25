# -*- coding: UTF-8 -*-
"""
title: 设计推特
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
Implement the Twitter class:
    Twitter() Initializes your twitter object.
    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]
Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


Constraints:
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 10^4
All the tweets have unique IDs.
At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""
import heapq
from collections import defaultdict, deque
from typing import List


class Twitter:
    """哈希表 + 队列 + 优先队列"""

    def __init__(self):
        self.user2tweets = defaultdict(deque)
        self.user2follows = defaultdict(set)
        self.capacity = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.user2tweets[userId]) == self.capacity:
            self.user2tweets[userId].pop()
        self.user2tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user2follows[userId].add(userId)
        queue = []
        for followee_id in self.user2follows[userId]:
            if self.user2tweets[followee_id]:
                queue.append((-self.user2tweets[followee_id][0][0], followee_id, 0))
        heapq.heapify(queue)
        res, cnt = [], 0
        while queue and cnt < self.capacity:
            _, followee_id, i = heapq.heappop(queue)
            res.append(self.user2tweets[followee_id][i][1])
            if i + 1 < len(self.user2tweets[followee_id]):
                heapq.heappush(queue, (-self.user2tweets[followee_id][i + 1][0], followee_id, i + 1))
            cnt += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user2follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user2follows[followerId].discard(followeeId)


if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 5)
    print(obj.getNewsFeed(1))
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    print(obj.getNewsFeed(1))
    obj.unfollow(1, 2)
    print(obj.getNewsFeed(1))
