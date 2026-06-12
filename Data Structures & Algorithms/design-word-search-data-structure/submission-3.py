class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                cur.children[ch] = TrieNode()  
                cur = cur.children[ch]
        cur.word = True      

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                ch = word[i]
                if ch==".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return True if cur.word else False
        return dfs(0,self.root)
        
# [day,bay,may,.ay]
# 10,000 n= 10*4
# {day,bay,may}
# search (.) => a~z true 26*26