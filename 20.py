class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        bracket_pair = {'(' : ')', '[' : ']', '{' : '}'}
        queue = []
        
        for c in s:
            if c in {'(', '{', '['}:
                queue.append(c)
            else:
                if len(queue) == 0:
                    return False
                
                bracket = queue[-1]
                if c is bracket_pair[bracket]:
                    del queue[-1]
                else:
                    return False
        
        if not queue:
            return True
