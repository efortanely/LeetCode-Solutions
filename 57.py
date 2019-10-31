class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            if i+1 < len(intervals) and intervals[i][0] <= intervals[i+1][0] and intervals[i+1][1] <= intervals[i][1]:
                intervals.remove(intervals[i+1])
            elif i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = intervals[i+1][1]
                intervals.remove(intervals[i+1])
            else:
                i += 1
        return intervals
