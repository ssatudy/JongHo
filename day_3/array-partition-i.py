class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, 1
        sum_nums = 0
        while right <= len(nums)-1:  
            sum_nums += min(nums[left], nums[right])
            left += 2
            right += 2
        return sum_nums