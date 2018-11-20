#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_temp = {}
        for i in range(len(s)):
            if s[i] in count_temp:
                count_temp[s[i]] = count_temp[s[i]] + 1
            else:
                count_temp[s[i]] = 1

        for i in range(len(s)):
            if count_temp[s[i]] == 1:
                return i

        return -1

