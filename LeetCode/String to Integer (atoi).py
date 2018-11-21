# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_max = 2 ** 31 - 1
        str_min = -2 ** 31
        temp = ''

        if str == '':
            return 0
        i = 0
        flag = 1
        if i < len(str):
            if str.isspace():  # 空格
                i += 1
            if str[i] == '-':  # 负数
                flag = -1
            if (str[i] == '-' or str[i] == '+'):  # 多个正负号+++---
                i += 1
            else:
                temp += str[i]
                i += 1

        temp = int(temp)
        if temp > str_max:
            return str_max
        elif temp < str_min:
            return str_min
        else:
            return temp
			

# 修改为以下代码
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()  # 删除首尾空格
        if str == "":
            return 0
        number = 0
        flag = 1  # 默认为正数
        # 判断首字符是否为正负号
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                number = 10 * number + ord(c) - ord('0')  # ord(c) 返回的是字符对应的 ASCII 码
            else:
                break
        number = flag * number
        if number < - 2 ** 31:
            return - 2 ** 31
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return number
