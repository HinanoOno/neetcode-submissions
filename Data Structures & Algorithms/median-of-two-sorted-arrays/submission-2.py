class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1),len(nums2)
        for i in range(m):
            heapq.heappush(nums1,nums2[i])
        total = n+m
        cur = 0
        if total%2:
            while cur<total//2+1:
                num = heapq.heappop(nums1)
                cur += 1
            return num
        else:
            while cur<total//2:
                num = heapq.heappop(nums1)
                cur += 1
            num2 = heapq.heappop(nums1)
            return (num+num2)/2

        