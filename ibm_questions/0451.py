from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(char * count for char, count in Counter(s).most_common())

if __name__ == "__main__":
    s = "loveleetcode"
    ans = Solution().frequencySort(s)
    print(ans)