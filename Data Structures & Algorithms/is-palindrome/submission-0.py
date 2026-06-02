class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy=''
        for char in s:
            if char.isalnum():
                copy+=char.lower()
        return copy==copy[::-1]
        