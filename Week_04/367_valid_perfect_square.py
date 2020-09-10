class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        x = num // 2
        while x ** 2 > num:
            x = (x + num // x) // 2
        return x ** 2 == num

    def binary_find(self, num):
        if num == 1:
            return True

        left, right = 0, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            elif mid ** 2 > num:
                right = mid - 1
        return False
    
    def algo(self, num):
        x = 1
        while num > 0:
            num -= x
            x += 2
        return num == 0
