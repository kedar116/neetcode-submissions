class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if j==i:
                    continue
                if numbers[i]+numbers[j]==target:
                    return [min(i,j)+1,max(i,j)+1]