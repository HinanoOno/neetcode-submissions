class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        for i in range(1,n):
            left[i] = max(left[i-1],height[i-1])
        for j in range(n-2,-1,-1):
            right[j] = max(right[j+1],height[j+1])
        ans = []
        for i in range(n):
            min_height = min(left[i],right[i])
            ans.append(max(0,min_height-height[i]))
        print(ans,left,right)
        return sum(ans)

# height = [0,2,0,3,1,0,1,3,2,1]
# left = [0,0,2,2,3,3,3,3,3,3]
# right = [3,3,3,3,3,3,3,3,2,1,0]
# result = [0,0,2,0,2,3,2,0,0,0,0]
# ans = 9
        