
class Trie:
    def __init__(self):
        self.children = {}
        self.data = None
        self.is_terminal = False

    def insert(self, word: str) -> None:
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = Trie()

            node = node.children[c]

        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self

        for c in word:
            if c not in node.children:
                return False

            node = node.children[c]

        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self

        for c in prefix:
            if c not in node.children:
                return False

            node = node.children[c]

        return True
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert(trie.search("apple") == True)
    assert(trie.search("app") == False)
    assert(trie.startsWith("app") == True)
    trie.insert("app")
    assert(trie.search("app") == True)

    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("beer")
    trie.insert("add")
    trie.insert("jam")