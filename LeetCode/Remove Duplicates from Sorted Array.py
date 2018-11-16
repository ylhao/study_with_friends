class Solution:
    def removeDuplicates(self, nums):
        """
    :type nums: List[int]
    :rtype: int
    """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        else:
            for i in range(len(nums) - 2):
                if nums[i] == nums[i + 1]:
                    del nums[i]
            return len(nums)
			

# 修改为以下代码
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        i = 1
        j = 1
        size = len(nums)
        while j < len(nums):
            if nums[j] == nums[i - 1]:
                 j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        return i
        
            
        
