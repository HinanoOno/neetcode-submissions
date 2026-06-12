class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def add(cur,open,close,i):
            nonlocal ans
            if i==n*2:
                if open==close:
                    ans.append(cur)
                return 
            if open>=close:
                add(cur+"(",open+1,close,i+1)
            if open>close:
                add(cur+")",open,close+1,i+1)
            return ans
        return add("",0,0,0)
            
        