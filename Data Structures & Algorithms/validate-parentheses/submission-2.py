class Solution:
    def isValid(self, s: str) -> bool:
        data = {"":")","{":"}","[":"]"}
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] in ["(","{","["]:
                stack.append(s[i])
            elif s[i]==")":
                if not stack:
                    return False
                ch = stack.pop()
                if ch!="(":
                    return False
            elif s[i]=="}":
                if not stack:
                    return False
                ch = stack.pop()
                if ch!="{":
                    return False
            elif s[i]=="]":
                if not stack:
                    return False
                ch = stack.pop()
                if ch!="[":
                    return False
        return True if not stack else False