#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count_temp = {}
        
		for x in s:
            if x in count_temp:
                count_temp[x] = count_temp[x] + 1
            else:
                count_temp[x] = 1
				
        for x in t:
            if x in count_temp and count_temp[x] != 0:
                count_temp[x] = count_temp[x] - 1
            else:
                return False
        
		return True