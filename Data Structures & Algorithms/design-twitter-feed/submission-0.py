class Twitter:

    def __init__(self):
        self.followMap = {} # (userId, followersId)
        self.tweetMap = {} # (userId, tweets)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [(self.count,tweetId)]
        else:
            self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        ids = [userId]
        
        if userId in self.followMap:
            ids.extend(self.followMap[userId])
        
        for i in ids:
            if i in self.tweetMap:
                feed.extend(self.tweetMap[i])
        
        feed.sort(reverse=True)
        
        res = []
        counter = 0
        for count, tweetId in feed:
            if counter == 10:
                break
            res.append(tweetId)
            counter += 1
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
