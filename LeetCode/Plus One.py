class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = (len(digits)) - 1
        while i >= 0:
            if i == 0:  # 一位
                if (digits[i] + 1) > 9:
                    digits[i] = 0
                    res = [1]
                    res.extend(digits)
                    return res

            if (digits[i] + 1) <= 9:  # 多位（最后一位不是9）
                digits[i] += 1
                return digits

            else:  # 多位（最后一位是9）
                digits[i] = 0
                i = i - 1

