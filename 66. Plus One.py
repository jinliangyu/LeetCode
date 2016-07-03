"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""


# Time: O(n)
# Space: O(1)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in xrange(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits



if __name__ == '__main__':
    digits = [1, 1, 8, 9, 9, 9]
    print Solution().plusOne(digits)