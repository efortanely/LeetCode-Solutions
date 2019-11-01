class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isword = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        if not word:
            return
        else:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isword = True
        

    def search(self, word: str) -> bool:
        return self.nodeSearch(self.root, word)
    
    def nodeSearch(self, node: TrieNode, word: str) -> bool:
        for i in range(len(word)):
            c = word[i]
            if c is '.':
                if i+1 < len(word):
                    is_word = False
                    for child in node.children:
                        is_word |= self.nodeSearch(node.children[child], word[i+1:])
                    return is_word
                else:
                    is_word = False
                    for child in node.children:
                        is_word |= node.children[child].isword
                    return is_word
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.isword


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
