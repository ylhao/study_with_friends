class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums
        for i in range(len(nums) - 1):
            if nums.count(nums[i]) == 1:
                return nums[i]


# 修改为以下代码
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
            