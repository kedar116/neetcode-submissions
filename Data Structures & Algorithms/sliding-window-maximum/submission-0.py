class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            max_so_far=-999999
            for j in range(i,len(nums)):
                if j-i+1==k:
                    window=nums[i:j+1]
                    for n in range(len(window)):
                        max_so_far=max(max_so_far, window[n])
                    res.append(max_so_far)

        return res
