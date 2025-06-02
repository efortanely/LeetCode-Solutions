from json import dumps

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.val = ""
        self.is_terminal = False

    def insert(self, word: str) -> None:
        node = self

        for c in word:
            idx = ord(c) - ord('a')

            if not node.children[idx]:
                node.children[idx] = Trie()

            node = node.children[idx]

        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self

        for c in word:
            idx = ord(c) - ord('a')

            if not node.children[idx]:
                return False

            node = node.children[idx]

        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self

        for c in prefix:
            idx = ord(c) - ord('a')

            if not node.children[idx]:
                return False

            node = node.children[idx]

        return True

    def __str__(self):
        to_str = ""

        while self.children:
            to_str += str(self.children.pop())
        
        return to_str

def visualize_trie(trie):
    """Visualizes the Trie as a branching tree structure."""
    graph = {
        "kind": {"graph": True},
        "nodes": [{"id": "root", "label": "root"}],
        "edges": []
    }
    
    def dfs(node, node_id, parent_id, prefix=""):
        if parent_id is not None:
            graph["edges"].append({"from": parent_id, "to": node_id})
        
        for i, child in enumerate(node.children):
            if child:
                char = child.val
                child_id = f"{prefix}{char}"
                graph["nodes"].append({"id": child_id, "label": char})  # Show only character in label
                dfs(child, child_id, node_id, child_id)
    
    dfs(trie, "root", None)
    
    return dumps(graph, indent=2)
    
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
    trie.insert("rental")

    visualize_trie(trie)

    assert(trie.search("apps") == False)
    assert(trie.search("app") == True)
    assert(trie.search("ad") == False)
    assert(trie.search("applepie") == False)
    assert(trie.search("rest") == False)
    assert(trie.search("jan") == False)
    assert(trie.search("rent") == True)
    # assert(trie.search("beer") == True)
    # assert(trie.search("jam") == True)
    # assert(trie.startsWith("apps") == True)
    # assert(trie.startsWith("app") == True)
    # assert(trie.startsWith("ad") == True)
    # assert(trie.startsWith("applepie") == False)
    # assert(trie.startsWith("rest") == True)
    # assert(trie.startsWith("jan") == True)
    # assert(trie.startsWith("rent") == True)
    # assert(trie.startsWith("beer") == True)
    # assert(trie.startsWith("jam") == True)
    # assert(trie.startsWith("ad") == True)
    # assert(trie.startsWith("applepie") == False)
    # assert(trie.startsWith("rest") == True)
    # assert(trie.startsWith("jan") == True)
    # assert(trie.startsWith("rent") == True)
    # assert(trie.startsWith("beer") == True)
    # assert(trie.startsWith("jam") == True)