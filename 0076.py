class Solution:
    def matches(self, seen, t):
        match = True
        t_dict = Counter(t)
        if t_dict.keys() != seen.keys():
            match = False
        else:
            for key, val in seen.items():
                if val < t_dict[key]:
                    match = False
                    break
        return match
    
    def minWindow(self, s: str, t: str) -> str:
        num_chars = float("inf")
        min_str = ""
        seen = dict()
        left = 0
        right = 0
        if len(t) == 1 and t in s:
            return t
        while right < len(s):
            while right < len(s) and not self.matches(seen, t):
                if s[right] in set(t):
                    seen[s[right]] = (seen[s[right]] if s[right] in seen else 0) + 1
                right += 1
            
            if self.matches(seen, t):
                if right - left + 1 < num_chars:
                    num_chars = right - left + 1
                    min_str = s[left:right]
            
            if s[left] in seen:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
            left += 1
            while self.matches(seen, t):
                if self.matches(seen, t):
                    if right - left + 1 < num_chars:
                        num_chars = right - left + 1
                        min_str = s[left:right]
                    
                if s[left] in seen:
                    seen[s[left]] -= 1
                    if seen[s[left]] == 0:
                        del seen[s[left]]
                left += 1
            
        return min_str
