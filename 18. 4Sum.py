import collections
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


# Time: O(n^3)
# Space: O(1)
# Time Limit Exceeded!!!
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k1 = j + 1
                k2 = len(nums) - 1
                while k1 < k2:
                    if nums[i] + nums[j] + nums[k1] + nums[k2] == target:
                        result.append([nums[i], nums[j], nums[k1], nums[k2]])
                        k1 += 1
                        k2 -= 1
                        while k1 < k2 and nums[k1] == nums[k1 - 1]:
                            k1 += 1
                        while k1 < k2 and nums[k2] == nums[k2 + 1]:
                            k2 -= 1
                    elif nums[i] + nums[j] + nums[k1] + nums[k2] > target:
                        k2 -= 1
                    else:
                        k1 += 1
        return result


# Time: O(n^2 * p)
# Space: O(n^2 * p)
# Hash solution.
class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                is_duplicated = False
                for [x, y] in lookup[nums[i] + nums[j]]:
                    if nums[x] == nums[i]:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    lookup[nums[i] + nums[j]].append([i, j])
        ans = {}
        for c in xrange(2, len(nums)):
            for d in xrange(c + 1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = "".join(str(quad))
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)
        return result


if __name__ == '__main__':
    S = [1, 0, -1, 0, -2, 2]
    print  Solution2().fourSum(S, 0)