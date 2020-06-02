class Solution:
    def calc_diff(self, word1: str, word2: str):
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                return char1, char2
        return None, None
    
    def graph_empty(self, in_degree):
        for v in in_degree.values():
            if v:
                return False
        return True
    
    def all_prefix_greater(self, words):
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) < len(word2):
                return False
        return True
    
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ''
        elif len(words) == 1:
            return words[0][::-1]
        ans = ''
        adj = dict()
        in_degree = dict()
        char_set = set([char for word in words for char in word])
        for char in char_set:
            adj[char] = []
            in_degree[char] = 0
            
        if len(in_degree) == 1:
            return list(in_degree.keys())[0]
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            key, val = self.calc_diff(word1, word2)
            
            if key and val:
                adj[key].append(val)
                in_degree[val] += 1
        
        if self.graph_empty(in_degree) and self.all_prefix_greater(words):
            return ''
        
        while in_degree.keys():
            zeroes = [k for k, v in in_degree.items() if v == 0]
            if not zeroes: #cycle detected
                return ''
            for k in zeroes:
                ans += k
                del in_degree[k]
                for neighbor in adj[k]:
                    in_degree[neighbor] -= 1
        
        return ans
