# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size1 = len(haystack)
        size2 = len(needle)
        if size2 == 0:
            return 0
        if size1 < size2:
            return -1
        i = 0
        while i < size1:
            if size1 - i < size2:
                return -1
            if haystack[i] == needle[0]:
                j = 1
                while j < size2:
                    if haystack[i + j] != needle[j]:
                        break
                    else:
                        j += 1
                if j == size2:
                    return i
            i += 1
        return -1