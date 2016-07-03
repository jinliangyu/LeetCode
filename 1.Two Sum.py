
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    # Approach #1 (Brute Force)
    # Time: O(n^2)
    # Space: O(1)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        print "no two number solution"


class Solution2(object):
    # Approach #2 (Two-pass Hash Table)
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums, target):
        adict = {}
        for i in range(len(nums)):
            adict[nums[i]] = i
        for num in nums:
            if (target - num) in adict and adict[target - num] != adict[num]:
                return [adict[num], adict[target - num]]
        print "no two number solution"


class Solution3(object):
    # Approach #3 (One-pass Hash Table)
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums, target):
        adict = {}
        for i in range(len(nums)):
            if target - nums[i] in adict:
                return [adict[target - nums[i]], i]
            adict[nums[i]] = i
        print "no two number solution"


def main():
    nums = [3,2,4]
    target = 6
    print "#1: ", Solution().twoSum(nums, target)
    print "#2: ", Solution2().twoSum(nums, target)
    print "#3: ", Solution3().twoSum(nums, target)
    print "#4: ", Solution4().twoSum(nums, target)


if __name__ == '__main__':
    main()