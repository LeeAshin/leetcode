class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set(nums)
        if len(list(set1)) != len(nums):
            return True
        else:
            return False