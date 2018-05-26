class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(nums)
        return lst[int(len(lst)/2)]