"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
indexed).

Once you pay the cost, you can either climb one or two steps. You need to find
minimum cost to reach the top of the floor, and you can either start from the
step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""


# f[i] = min[f[i-1], f[i-2]] + cost[i]
# f[-1] = min[f[-2], f[-3]+cost[-1])
class Solution1(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f = [cost[0], cost[1]]
        for i in range(2, len(cost) - 1):
            f.append(min(f[i - 1], f[i - 2]) + cost[i])
        f.append(min(f[-1], f[-2] + cost[-1]))
        return f[-1]


# f[i] = cost[i] + min(f[i+1], f[i+2])
class Solution2(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)


if __name__ == '__main__':
    cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # print Solution1().minCostClimbingStairs(cost)
    print Solution2().minCostClimbingStairs(cost)
