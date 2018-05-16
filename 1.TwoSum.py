class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            d = target - i
            if d in nums[nums.index(i) + 1::]:
                res = nums[nums.index(i) + 1:]
                return [nums.index(i), res.index(d) + nums.index(i) + 1]
            else:
                continue
