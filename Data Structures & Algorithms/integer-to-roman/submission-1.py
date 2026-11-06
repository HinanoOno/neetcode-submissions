import bisect
class Solution:
    def intToRoman(self, num: int) -> str:
        data ={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        ans =""
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        while num>0:
            idx = bisect.bisect_right(numbers,num)
            if idx-1>=len(numbers):
                target = 1000
            else:
                target = numbers[idx-1]
            #print(idx,target)
            times = num//target
            ans += data[target]*times
            num = num-(target*times) 
        return ans
            