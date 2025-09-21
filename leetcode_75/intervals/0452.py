from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 1
        shots = 1
        max_x = points[0][1]

        while i < len(points):
            curr_x_min = points[i][0]
            curr_x_max = points[i][1]

            if curr_x_min > max_x:
                shots += 1
                max_x = curr_x_max
            else:
                max_x = min(max_x, curr_x_max)

            i += 1
        
        return shots

if __name__ == "__main__":
    points = [[1,2],[2,3],[3,4],[4,5]]
    ans = Solution().findMinArrowShots(points)
    assert ans == 2