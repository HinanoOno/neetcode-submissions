class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l,r = 0,mountainArr.length()-1
        split = 0
        while l<=r:
            mid = (l+r)//2
            l_v = mountainArr.get(mid-1) if mid-1>=0 else -1
            r_v = mountainArr.get(mid+1) if mid+1<n else -1
            mid_v = mountainArr.get(mid)
            if l_v<mid_v and mid_v>r_v:
                split = mid
                break
            elif mid_v>r_v:
                r = mid-1
            else:
                l = mid+1
        print(split)
        def search(l,r):
            nonlocal mountainArr
            while l<=r:
                mid = (l+r)//2
                if mountainArr.get(mid) == target:
                    return mid
                elif mountainArr.get(mid)<target:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        def search2(l,r):
                nonlocal mountainArr
                while l<=r:
                    mid = (l+r)//2
                    if mountainArr.get(mid) == target:
                        return mid
                    elif mountainArr.get(mid)>target:
                        l = mid+1
                    else:
                        r = mid-1
                return -1
        if mountainArr.get(split) == target:
            return split
        left = search(0,split)
        right = search2(split,n-1)
        #print(left,right)
        if left!=-1:
            return left
        elif right!=-1:
            return right
        else:
            return -1

