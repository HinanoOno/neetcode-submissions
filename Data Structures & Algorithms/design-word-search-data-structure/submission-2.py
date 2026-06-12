class WordDictionary:

    def __init__(self):
        self.data = set()
        

    def addWord(self, word: str) -> None:
        self.data.add(word)
        

    def search(self, word: str) -> bool:
        n = len(word)
        candidate = set()

        def dfs(cur,i):
            if i==n:
                candidate.add(cur)
                return 
            if word[i]==".":
                for j in range(26):
                    ch = chr(ord("a")+j)
                    #print(ch)
                    dfs(cur+ch,i+1)
            else:
                dfs(cur+word[i],i+1)
        dfs("",0)
        
        for c in candidate:
            if c in self.data:
                return True
        return False


        
# [day,bay,may,.ay]
# 10,000 n= 10*4
# {day,bay,may}
# search (.) => a~z true 26*26