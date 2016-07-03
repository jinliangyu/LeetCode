"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""


class Solution(object):
    # Time: O(n)
    # Space: O(1)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] == target:
                found = True
                return True
        return False


class Solution2(object):
    # Time: O(log(n))
    # Space: O(1)
    def search(self, nums, target):
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) / 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[first]:
                first += 1
            elif nums[mid] > nums[first]:
                if nums[first] <= target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[mid] < target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1
        return False



if __name__ == '__main__':
    # nums = [0, 1, 2, 4, 5, 6, 7]
    # target = 2
    nums = [1,3,1,1,1]
    target = 3
    print Solution2().search(nums, target)
