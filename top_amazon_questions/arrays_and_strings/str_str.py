class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        
        return -1
        
def main():
    runner = Solution()
    haystack = "mississippi"
    needle = "issip"
    ans = runner.strStr(haystack, needle)
    print(ans)

if __name__ == "__main__":
    main()