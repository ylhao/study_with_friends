# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == '':
            return True
        
        # 移除其它字符
        stemp = ''
        for i in range(len(s)):
            if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z' or s[i] >= '0' and s[i] <= '9':
                stemp += s[i]
        
        stemp = stemp.lower()  # 大写转小写
        
        # 判断
        i = 0
        j = len(stemp) - 1
        while(i < j):
            if(stemp[i] != stemp[j]):
                return False
            else:
                i += 1
                j -= 1
                
        return True