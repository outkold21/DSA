class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=str(x)
        return i == i[::-1]
