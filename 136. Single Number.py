"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Subscribe to see which companies asked this question
"""


import operator
# Time: O(n)
# Space: O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for k, v in d.iteritems():
            if v == 1:
                return k


# Time: O(n)
# Space: O(1)
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            x ^= i
        return x


# fastest
# Time: O(n)
# Space: O(1)
class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return reduce(lambda x, y: x ^ y, nums)
        return reduce(operator.xor, nums)


if __name__ == '__main__':
    nums = [1,2,3,3,2,1,4,5,5]
    print Solution3().singleNumber(nums)
