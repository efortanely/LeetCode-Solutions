from collections import defaultdict

class Trie:
    def __init__(self):
        self.trie = defaultdict(dict)

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word + "#":
            if c not in curr:
                curr[c] = defaultdict(dict)
            curr = curr[c]

    def search(self, word: str) -> bool:
        return self.startsWith(word + "#")

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
def main():
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))

if __name__ == "__main__":
    main()