class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi = 1
        multi_lst = []
        if nums.count(0) > 1:  
            return [0] * len(nums)
        elif nums.count(0) == 1:  
            for i in range(len(nums)):  
                if nums[i] != 0:  
                    multi *= nums[i]
                else:  
                    multi *= 1
            for j in range(len(nums)):  
                if nums[j] == 0:  
                    multi_lst.append(multi)
                else:  
                    multi_lst.append(0)
        else:  
            for k in nums:  
                multi *= k
            for l in nums:  
                multi_lst.append(int(multi/l))
        return multi_lst