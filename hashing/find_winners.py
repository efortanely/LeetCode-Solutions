from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        players = set()

        for match in matches:
            losers[match[1]] += 1
            players.add(match[0])
            players.add(match[1])
        
        return [sorted(list(players.difference(losers.keys()))), sorted([key for key, value in losers.items() if value == 1])]
        
def main():
    runner = Solution()

    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    ans = runner.findWinners(matches)
    print(ans)

if __name__ == "__main__":
    main()