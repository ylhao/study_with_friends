#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for x in nums:
            if x != 0:
                nums[k] = x
                k += 1
        nums[k:] = [0] * (len(nums) - k)
        #return nums