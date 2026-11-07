class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero = s.count("0")
        one = s.count("1")

        if one==1:
            return str(0)*zero+str(1)
        else:
            return str(1)*(one-1)+str(0)*zero+str(1)
        