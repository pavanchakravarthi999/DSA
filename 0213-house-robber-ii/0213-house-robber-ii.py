class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for money in houses:
                prev1, prev2 = max(prev1, prev2 + money), prev1
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
