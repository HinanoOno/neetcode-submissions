class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry=0
        for i in range(n-1,-1,-1):
            if i==n-1:
                digits[i]+=(1+carry)
            else:
                digits[i]+=carry
            carry = 0
            if  digits[i]>=10:
                carry = digits[i]//10
                digits[i]= digits[i]%10
        if carry>0:
            return [carry]+digits
        return digits
        