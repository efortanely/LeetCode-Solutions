from functools import cache

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        @cache
        def dp(i, feed):
            if i == minutesToTest:
                return 0
            
            if feed:
                ans = dp(i+1)
            else:
                ans = dp(i)

            return ans
            # recurrence relation
            # 0..N pigs feed pig or don't feed pig
            # i what minute it is
            # start at minute 0...N
            # RR = 
            pass
        
        return dp(0, feed=True)
    
    # feed pigs
    # 1 chose pigs to feed
    # 2 chose which buckets to feed each pig
    # 3 wait minutesToDie - no feeding
    # 4 pigs fed poison die
    # 5 repeat until run out of time
    # determine minimum number of pigs needed to determine which bucket is poisonous

if __name__ == "__main__":
    runner = Solution()
    buckets = 4
    minutesToDie = 15
    minutesToTest = 15

    ans = runner.poorPigs(buckets, minutesToDie, minutesToTest)
    print(ans)