class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        ans = 0

        for alt in gain:
            altitude += alt
            ans = max(ans, altitude)
    
        return ans