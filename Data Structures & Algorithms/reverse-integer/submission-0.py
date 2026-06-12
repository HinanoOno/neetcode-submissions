class Solution:
    def reverse(self, x: int) -> int:
        flg = False 
        max_v = 2**31-1
        if x<0:
            x = -x
            flg = True
        tmp = int(str(x)[::-1]) 
        if flg and tmp>max_v:
            return 0
        elif flg:
            return -int(str(x)[::-1])
        elif tmp>max_v-1:
            return 0
        else:
            return int(str(x)[::-1])