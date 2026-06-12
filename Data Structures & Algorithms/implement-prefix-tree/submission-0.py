class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def insert(self, word: str) -> None:
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = PrefixTree()
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True if cur.isWord else False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True 
        
        