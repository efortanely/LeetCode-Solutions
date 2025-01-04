class Solution:
    def is_unique(self, tup):
        s = set()
        for string in tup:
            if len(s.intersection(set(string))) != 0:
                return False
            s = s.union(set(string))
        return True
    
    def str_len(self, tup):
        return sum(map(lambda string: len(string), tup))
    
    def prune_copies(self, arr):
        retlist = []
        for a in arr:
            unq = True
            s = set()
            for ch in a:
                if ch in s:
                    unq = False
                    break
                else:
                    s.add(ch)
            if unq:
                retlist.append(a)
        return retlist
    
    def maxLength(self, arr: List[str]) -> int:
        max_length = 0
        arr = self.prune_copies(arr)
        
        for i in range(1, len(arr)+1):
            l = list(combinations(arr, i))
            if i == 1:
                max_length = max(map(lambda tup: len(tup[0]), l))
            else:
                for tup in l:
                    if self.is_unique(tup):
                        max_length = max(max_length, self.str_len(tup))
        return max_length
