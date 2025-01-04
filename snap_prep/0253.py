class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        
        end_times = []
        heapq.heappush(end_times, intervals[0][1])
        
        for interval in intervals[1:]:
            cur_start, prev_end = interval[0], end_times[0]
            if cur_start >= prev_end:
                heapq.heappop(end_times)
            heapq.heappush(end_times, interval[1])
        
        return len(end_times)
