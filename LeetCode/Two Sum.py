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



####################################################
# 2018/11/20 修改
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = nums.copy()
        nums1 = sorted(nums1)
		
        left = 0
        right = len(nums1) - 1
        dict_tmp = {}

        while left <= right:
            if nums1[left] + nums1[right] > target:
                right -= 1
            elif nums1[left] + nums1[right] < target:
                left += 1
            else:
                for x in range(len(nums)):
                    if nums[x] == nums1[left]:
                        for y in range(len(nums)):
                            if nums[y] == nums1[right] and x != y:
                                return x, y
								
								
# 修改为以下代码

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = nums.copy()
        nums1 = sorted(nums1)
		
        left = 0
        right = len(nums1) - 1
        dict_tmp = {}

        while left <= right:
            if nums1[left] + nums1[right] > target:
                right -= 1
            elif nums1[left] + nums1[right] < target:
                left += 1
            else:
                break
            
        res = []
        
        for x in range(len(nums)):
            if nums[x] == nums1[left] or nums[x] == nums1[right]:
                res.append(x)
        
        return res


