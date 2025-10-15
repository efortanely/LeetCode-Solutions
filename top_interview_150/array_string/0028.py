class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if __name__ == "__main__":
    haystack = "sabutsad"
    needle = "sad"
    ans = Solution().strStr(haystack, needle)
    print(ans)