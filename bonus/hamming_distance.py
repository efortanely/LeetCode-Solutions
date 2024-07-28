class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bits = x ^ y
        mask = 1
        ans = 0

        while mask <= bits:
            ans += bool(bits & mask)
            mask <<= 1
        
        return ans

def main():
    runner = Solution()
    x = 3
    y = 1
    ans = runner.hammingDistance(x, y)
    print(ans)

if __name__ == "__main__":
    main()