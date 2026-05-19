from collections import defaultdict
from typing import List
import heapq


class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        relevant_users = self.following[userId] | {userId}

        heap = []
        feed = []

        for uid in relevant_users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                timestamp, tweet_id = self.tweets[uid][idx]
                heapq.heappush(heap, (-timestamp, tweet_id, idx, uid))

        while heap and len(feed) < 10:
            _, tweet_id, idx, uid = heapq.heappop(heap)
            feed.append(tweet_id)

            idx -= 1
            if idx >= 0:
                timestamp, tweet_id = self.tweets[uid][idx]
                heapq.heappush(heap, (-timestamp, tweet_id, idx, uid))

        return feed