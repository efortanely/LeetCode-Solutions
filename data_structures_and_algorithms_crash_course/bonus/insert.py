from typing import List
import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        idx = bisect.bisect_left(intervals, newInterval)
        intervals = intervals[:idx] + [newInterval] + intervals[idx:]

        for interval in intervals:
            if ans and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)

        return ans

def main():
    runner = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    ans = runner.insert(intervals, newInterval)
    print(ans)

if __name__ == "__main__":
    main()