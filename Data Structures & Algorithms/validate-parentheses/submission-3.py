class Solution:
    def isValid(self, s: str) -> bool:
        data = {")":"(","}":"{","]":"["}
        n = len(s)
        stack = []
        
        for i in range(n):
            if stack and s[i] in data:
                num = stack.pop()
                if num != data[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False

                