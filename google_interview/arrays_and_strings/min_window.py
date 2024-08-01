from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def condition():
            for key, count in t_counter.items():
                if s_counter[key] < count:
                    return False
            
            return True
        
        left = right = 0
        min_window = float("inf")
        ans = ""
        s_counter = defaultdict(int)
        t_counter = Counter(t)

        for left in range(len(s)):
            while right < len(s) and not condition():
                s_counter[s[right]] += 1
                right += 1

            if condition() and right - left < min_window:
                min_window = right - left
                ans = s[left:right]

            s_counter[s[left]] -= 1

        return ans

def main():
    runner = Solution()
    s = "a"
    t = "aa"
    ans = runner.minWindow(s, t)
    print(ans)

if __name__ == "__main__":
    main()