class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        data = [0]*(n+1)
        data[0] = 1
        for i in range(1,n+1):
            print(int(s[i-1:i]))
            if i-2>=0 and 10<=int(s[i-2:i])<=26:
                data[i] += data[i-2]
            if i-1>=0 and 1<=int(s[i-1:i])<=9:
                data[i] += data[i-1]
            print(data)
        return data[-1]


        