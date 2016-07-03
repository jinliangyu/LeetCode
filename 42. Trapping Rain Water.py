# -*- coding: utf-8 -*-
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""


# Time:  O(n)
# Space: O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        top = 0
        for i in xrange(len(height)):
            if height[top] < height[i]:
                top = i
        second_top = 0
        for i in xrange(top):
            if height[second_top] < height[i]:
                second_top = i
            result += height[second_top] - height[i]
        second_top = len(height) - 1
        for i in reversed(xrange(top, len(height))):
            if height[second_top] < height[i]:
                second_top = i
            result += height[second_top] - height[i]
        return result


# Time: O(n)
# Space: O(n)

class Solution2(object):
    def trap(self, height):
        result = 0
        stack = []
        for i in xrange(len(height)):
            mid_height = 0
            while stack:
                [pos, h] = stack.pop()
                result += (min(h, height[i]) - mid_height) * (i - pos - 1)
                mid_height = h
                if height[i] < h:
                    stack.append([pos, h])
                    break
            stack.append([i, height[i]])
        return result


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print Solution().trap(height)
    print Solution2().trap(height)
