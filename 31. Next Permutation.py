# -*- coding:utf-8 -*-
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


# Time: O(n)
# Space: O(1)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        k = j
                nums[i], nums[k] = nums[k], nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                break
            if i == 0:
                nums.reverse()

class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in xrange(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                k = i
        if k == -1:
            nums.reverse()
            return
        for i in xrange(k + 1, len(nums)):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = nums[:k:-1]


if __name__ == '__main__':
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print nums
