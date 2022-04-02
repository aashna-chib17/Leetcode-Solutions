class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num = num**0.5
        if num - int(num) == 0:
            return True
        else:
            return False
