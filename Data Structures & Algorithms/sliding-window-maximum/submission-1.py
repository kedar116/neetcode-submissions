class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n-k+1):
            max_so_far=-999999
            for j in range(i,i+k):
                max_so_far=max(max_so_far, nums[j])
            res.append(max_so_far)

        return res
