class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if not digits:
            return [1]

        if digits[n-1]<9:
            digits[n-1]+=1
            return digits
        else:
            digits[n-1]=0
            return self.plusOne(digits[:n-1]) + [0]