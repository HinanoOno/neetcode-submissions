class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs",
        "8":"tuv","9":"wxyz"}

        n = len(digits)
        ans = []
        
        def dfs(cur,i):
            print(cur,i)
            if i==n and len(cur)==n:
                ans.append(cur)
            for j in range(i,n):
                for k in data[digits[j]]:
                    dfs(cur+k,j+1)
        dfs("",0)
        if not digits:
            return []
        return ans
        