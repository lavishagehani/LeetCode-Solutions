class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0
        while(num > 0):
            remainder = num % 10
            result = result * 10 + remainder
            num //= 10
        if result == x:
            return True
        return False 