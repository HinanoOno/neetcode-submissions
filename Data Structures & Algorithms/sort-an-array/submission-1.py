import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,r):
            n,m  = len(l),len(r)
            i,j = 0,0
            ans = []
            while i<n and j<m:
                if l[i]<r[j]:
                    ans.append(l[i])
                    i+=1
                elif l[i]==r[j]:
                    ans.append(l[i])
                    i+=1
                    ans.append(r[j])
                    j+=1
                else:
                    ans.append(r[j])
                    j+=1
            while i<n:
                ans.append(l[i])
                i+=1
            while j<m:
                ans.append(r[j])
                j+=1
            print(ans,l,r)
            return ans

        def mergeSort(nums):
            n = len(nums)
            if n<=1:
                return nums
            l,r = 0,n-1
            mid = (l+r)//2
            print(l,r,mid)
            left = mergeSort(nums[l:mid+1])
            right = mergeSort(nums[mid+1:r+1])
            return merge(left,right)
        return mergeSort(nums)


