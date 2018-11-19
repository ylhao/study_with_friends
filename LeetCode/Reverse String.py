#Reverse String
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
		

# 第二种解法		
class Solution:
def reverseString(self, s):
	"""
	:type s: str
	:rtype: str
	"""
	i = 0
	j = len(s) - 1
	s = list(s)
	while(i < j):
		temp = s[i]
		s[i] = s[j]
		s[j] = temp
		i += 1
		j -= 1
	return ''.join(s)