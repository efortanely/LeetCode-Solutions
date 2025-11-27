from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 0

        while i < len(intervals) - 1:
            end = intervals[i][1]
            start = intervals[i+1][0]

            if end >= start:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.remove(intervals[i+1])
            else:
                i += 1
        return intervals

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    ans = Solution().merge(intervals)
    print(ans)