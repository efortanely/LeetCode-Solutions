from typing import List
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        balloon_count = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        num_balloons_fit = []

        for ch, count in balloon_count.items():
            num_balloons_fit += [counts[ch] // count]

        return min(num_balloons_fit)
    
def main():
    runner = Solution()

    text = "loonbalxballpoon"
    ans = runner.maxNumberOfBalloons(text)
    print(ans)

if __name__ == "__main__":
    main()