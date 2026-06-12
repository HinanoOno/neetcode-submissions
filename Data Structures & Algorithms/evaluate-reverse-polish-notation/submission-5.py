class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i in range(n):
            if tokens[i] in {"+","-","*","/"}:
                f = stack.pop()
                s = stack.pop()
                if tokens[i] == "+":
                    tmp = s+f
                elif tokens[i] =="-":
                    tmp = s-f
                elif tokens[i] =="*":
                    tmp = s*f
                else:
                    tmp = s/f
                    tmp = int(tmp)
                stack.append(tmp)
            else:
                stack.append(int(tokens[i]))
            print(stack)
        return stack[0]