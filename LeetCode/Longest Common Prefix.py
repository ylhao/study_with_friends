#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            for astr in strs:
                if astr[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
		
		
# 修改为以下代码

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ''
        
        # 找出最短长度
        minLen = len(strs[0])
        for str in strs[1:]:
            strLen = len(str)
            if strLen < minLen:
                minLen = strLen
        
        # 找出共同序列
        res = ''
        for i in range(minLen):
            c = strs[0][i]
            flag = True
            for str in strs[1:]:
                if str[i] != c:
                    flag = False
                    break
            if flag:
                res += c
            else:
                return res
        return res
                    
                