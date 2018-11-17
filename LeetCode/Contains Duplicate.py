class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''超时了
        if len(nums) < 2:
            return False
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                return True
        return False
        '''
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False