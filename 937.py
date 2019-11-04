class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key=self.sort)
        return logs
    
    def sort(self, log):
        ident, content = log.split(" ", 1)
        return (0, content, ident) if content[0].isalpha() else (1,)
