class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0:
            return nums1
        if len(nums2) == 0:
            return nums2
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
        return res
				
# 修改为以下代码
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0:
            return nums1
        if len(nums2) == 0:
            return nums2
			
        # 统计 nums1 数组中每个数字出现的次数
        count_map = {}
        for x in nums1:
            if x in count_map:
                count_map[x] = count_map[x] + 1
            else:
                count_map[x] = 1		
				
        res = []
        for x in nums2:
            if x in count_map and count_map[x] != 0:
                res.append(x)
                count_map[x] = count_map[x] - 1
        return res
 




  
       