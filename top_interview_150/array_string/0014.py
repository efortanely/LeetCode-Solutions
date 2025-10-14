from typing import List

class TrieNode:
    def __init__(self):
        self.data = None
        self.children = {}
        self.word_count = 0

def build_trie(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.word_count += 1
    
    return root

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs:
            return ""
        
        trie = build_trie(strs)
        prefix = []
        curr = trie
        total_words = len(strs)

        while len(curr.children) == 1:
            char = list(curr.children.keys())[0]
            curr = curr.children[char]
            if curr.word_count == total_words:
                prefix.append(char)
            else:
                break

        return "".join(prefix)

if __name__ == "__main__":
    strs = ["ab", "a"]
    ans = Solution().longestCommonPrefix(strs)
    print(ans)