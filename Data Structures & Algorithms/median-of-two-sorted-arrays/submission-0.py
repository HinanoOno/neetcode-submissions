class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1),len(nums2) #1,2
        s,h = [],[]

        for i in range(n):
            if not s or -s[0]>nums1[i]:
                heapq.heappush(s,-nums1[i])
            else:
                heapq.heappush(h,nums1[i])
            
        for i in range(m):
            if not s or -s[0]>nums2[i]:
                heapq.heappush(s,-nums2[i])
            else:
                heapq.heappush(h,nums2[i])
        print(s,h)
        while len(s)>len(h)+1:
            num = heapq.heappop(s)
            heapq.heappush(h,-num)
        while len(s)<len(h):
            num = heapq.heappop(h)
            heapq.heappush(s,-num)
        print(s,h)
        if len(s) == len(h):
            return (-s[0]+h[0])/2
        else:
            return -s[0]
        