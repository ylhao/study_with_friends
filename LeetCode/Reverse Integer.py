#Reverse Integer
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            y = int(str(x)[::-1])
        else:
            x = abs(x)
            y = -1 * (int(str(x)[::-1]))
        if y > 2147483637 or y < -2147483637:
            y = 0
        return y


# 另一种解法
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        flag = False
        
        if x < 0:
            x = abs(x)
            flag = True
        
        res = 0
        
        while(x != 0):
            res = (res * 10) + (x % 10)
            x = x // 10
        
        if flag:
            res = -res
        
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            res = 0
        
        return res