class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sr = list(str(x))
        return int("".join(sr[::-1])) == x