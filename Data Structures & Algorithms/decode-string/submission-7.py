class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        st = []
        cnt = []
        cur = ""
        k = 0
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                st.append(k)
                cnt.append(cur)
                k = 0
                cur = ""
            elif c=="]":
                tmp = cur
                num = st.pop()
                cur = cnt.pop()
                cur += tmp*num
            else:
                cur+=c
        return cur
