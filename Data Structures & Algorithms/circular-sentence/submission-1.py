class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        data = sentence.split()
        prev = data[0][-1]
        for i in range(1,len(data)):
            if data[i][0] !=prev:
                return False
            prev = data[i][-1]
        if prev!=data[0][0]:
            return False
        return True

        
