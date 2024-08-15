class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return len([stone for stone in stones if stone in jewels])
        
def main():
    runner = Solution()

    jewels = "aA"
    stones = "aAAbbbb"
    ans = runner.numJewelsInStones(jewels, stones)
    print(ans)

if __name__ == "__main__":
    main()