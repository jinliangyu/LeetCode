"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


# Time:  O(n)
# Space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for x in nums:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for x in nums:
            one = (one ^ x) & ~two
            two = (two ^ x) & ~one
        return one


# easy to understand
class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for x in nums:
            two |= one & x
            one ^= x
            three = one & two
            one &= ~three
            two &= ~three
            print one, two, three
        return one


if __name__ == '__main__':
    nums = [1,2,2,1,2,3,3,1,5,3]
    print Solution3().singleNumber(nums)
