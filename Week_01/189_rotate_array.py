class Solution1:
    """
    O(n^2)
    34/35
    timeout
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            r = nums[-1]
            for i in range(len(nums) - 1):
                nums[-i - 1] = nums[-i - 2]
            nums[0] = r
            k -= 1

class Solution2:
    """
    O(n)
    pass
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums) 
        if k <= 0:
            return nums
        n = len(nums)
        temp = nums[-k:] 
        nums[k:] = nums[: n - k]
        nums[:k] = temp
        
        
class Solution3:
    """
    O(n)
    pass
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1