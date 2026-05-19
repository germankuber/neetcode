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
        
        users_ids = self.following[userId] | {userId}
        
        list_sorted = []
        heapq.heapify(list_sorted)
        to_return = []
        for user_id in users_ids:
            if len(self.tweets[user_id]) > 0:
                last_twit_time, last_twit_id = self.tweets[user_id][-1]
                tweet_position = len(self.tweets[user_id]) - 1
                heapq.heappush(list_sorted, (-last_twit_time, last_twit_id, tweet_position, user_id))
                
        
        while len(list_sorted) > 0 and len(to_return) < 10:
            
            _, twit_id, tweet_position, user_id = heapq.heappop(list_sorted)
            to_return.append(twit_id)
            tweet_position -= 1
            if tweet_position >= 0:
                last_twit_time, last_twit_id = self.tweets[user_id][tweet_position]
                heapq.heappush(list_sorted, (-last_twit_time, last_twit_id, tweet_position, user_id))
        
        return to_return   