class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
        x = abs(x)
        lst = list(str(x))
        res = -int("".join(lst[::-1])) if negative else int("".join(lst[::-1]))
        return res if -2**31 <= res <= 2**31 - 1 else 0




        