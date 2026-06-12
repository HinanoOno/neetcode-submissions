class Twitter:

    def __init__(self):
        self.data =defaultdict(list)
        self.followes =defaultdict(set)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.data[userId].append((self.time,tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.data[userId][:]
        for f in self.followes[userId]:
            feed.extend(self.data[f][:])
        feed.sort(key = lambda x:-x[0])
        return [tweetId for _,tweetId in feed[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId ==followeeId:
            return 
        self.followes[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followes[followerId].discard(followeeId)