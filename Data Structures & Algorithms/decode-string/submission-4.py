class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        nums = set("1234567890")
        i = 0
        while i<n:
            if  s[i] in nums:
                cnt = 0
                while s[i] in nums:
                    cnt = cnt*10+int(s[i])
                    i+=1
                stack.append(str(cnt))
            elif s[i].isalpha():
                stack.append(s[i])
            elif s[i]=="[":
                pass
            elif s[i]=="]":
                cur = ""
                while stack and stack[-1].isalpha():
                    ch = stack.pop()
                    cur = ch+cur
                cnt = 0
                if stack and stack[-1].isnumeric():
                    num = stack.pop()
                    cnt = cnt*10+int(num)
                stack.append(cur*cnt)
            i+=1
            print(i,stack)
        return "".join(stack)
# 2a3b
# 2abbb
                

        