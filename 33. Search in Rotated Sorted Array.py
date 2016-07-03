"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    # Time: O(n)
    # Space: O(1)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        found = False
        for i in range(len(nums)):
            if nums[i] == target:
                found = True
                return i
        return -1

class Solution2(object):
    # Binary Search
    # Time: O(log(n))
    # Space: O(1)
    def search(self, nums, target):
        found = False
        first = 0
        last = len(nums) - 1
        while first <= last and not found:
            mid = (first + last) // 2
            if nums[mid] == target:
                found = True
                return mid
            else:
                if nums[first] <= nums[mid]:
                    if nums[first] <= target < nums[mid]:
                        last = mid
                    else:
                        first = mid + 1
                else:
                    if nums[mid] < target <= nums[last]:
                        first = mid + 1
                    else:
                        last = mid
        return -1


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 6, 7]
    target = 2
    print Solution2().search(nums, target)
