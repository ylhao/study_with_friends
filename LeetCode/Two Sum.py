#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        nums=sorted(nums)
        s=len(nums)
        for i in range(len(nums)):
            if nums[i]+nums[s] > target: 
                s=s-1
            elif i+nums[s] < target:
                i=i+1
            else:
                return i
        return False
        '''  # 超时
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return left, right
        return False
		
		
# 修改为以下代码
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_temp = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict_temp:
                return [dict_temp[target - x], i]
            dict_temp[x] = i
        return [-1, -1]
