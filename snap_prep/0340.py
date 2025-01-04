class CharacterSet:
    def __init__(self):
        self.seen = dict()
    
    def add(self, char: str):
        self.seen[char] = (self.seen[char] if char in self.seen else 0) + 1
        
    def remove(self, char: str):
        if char in self.seen:
            self.seen[char] -= 1
            if self.seen[char] == 0:
                del self.seen[char]
    
    def k_char(self, k: int):
        return len(self.seen.keys()) <= k
    
    def num_chars(self):
        return sum(self.seen.values())
    
    def get_dict(self):
        return self.seen

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k or not s:
            return 0
        
        left, right = 0, 0
        max_str = 0
        c = CharacterSet()
        
        c.add(s[right])
        
        if c.k_char(k):
            max_str = max(max_str, 1)
        
        while left <= right:
            if c.k_char(k) and right < len(s) - 1:
                right += 1
                c.add(s[right])
            else:
                c.remove(s[left])
                left += 1
            
            if c.k_char(k):
                max_str = max(max_str, c.num_chars())
        
        return max_str
