class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            if customers[i]=="Y":
                dp[i]+=1
        cnts = [0]*(n+1)
        print(dp)
        cnts[0] = sum(dp)
        for i in range(1,n+1):
            plus = 1 if dp[i-1]==1 else -1
            cnts[i] = cnts[i-1]-plus
        print(cnts)
        min_v = min(cnts)
        for i in range(n+1):
            if cnts[i]==min_v:
                return i

            
        