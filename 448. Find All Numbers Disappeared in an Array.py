class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        set1 = set(nums)
        set2 = set(range(1,n+1))
        return list(set2 - set1)
