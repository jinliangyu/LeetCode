"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == -b:
            return 0
        if a >= 0 and b >= 0:
            return self.add(a, b)
        elif a < 0 and b > 0:
            return -self.sub(-a, b)
        elif a > 0 and b < 0:
            return self.sub(a, -b)
        else:
            return -self.add(a, b)

    def add(self, a, b):
        if b == 0:
            return a
        else:
            sum  = a ^ b
            carry = (a & b) << 1
            return self.add(sum, carry)


    def sub(self, a, b):
        return self.add(a, self.add(~b, 1))


# Kogge–Stone adder
# Time: O(log n)
# Space: O(1)
class Solution2(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        p, g, i = a ^ b, a & b, 1
        while True:
            if (g << 1) >> i == 0:
                return a ^ b ^ (g << 1)
            if ((p | g) << 2) >> i == ~0:
                return a ^ b ^ ((p | g) << 1)
            p, g, i = p & (p << i), (p & (g << i)) | g, i << 1
if __name__ == '__main__':
    a = 14
    b = -16
    print Solution2().getSum(a, b)
