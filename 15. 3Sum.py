"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    # Time: O(n^2)
    # Space: O(1)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # if len(nums) < 3:
        #     return result
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and nums[k] == nums[k + 1] and j < k:
                        j += 1
        return result


class Solution2(object):
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result

if __name__ == '__main__':
    S = [-1, 0, 1, 2, -1, -4]
    print Solution2().threeSum(S)

