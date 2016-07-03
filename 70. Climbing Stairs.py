"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


# Time: O(n)
# Space: O(1)
# Fibonacci
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return b


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 5 ** 0.5
        return int((((1+s)/2)**(n+1) + ((1-s)/2)**(n+1)+ 0.5)/s)



if __name__ == '__main__':
    n = 4
    # n = 100
    print Solution2().climbStairs(n)