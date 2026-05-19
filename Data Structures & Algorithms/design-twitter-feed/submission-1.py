import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        usuarios = self.following[userId] | {userId}
        
        heap = []
        for u in usuarios:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (-time, tweetId, u, idx))
        
        feed = []
        while heap and len(feed) < 10:
            _, tweetId, u, idx = heapq.heappop(heap)
            feed.append(tweetId)
            
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (-time, tweetId, u, idx))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)