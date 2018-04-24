class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(nums)
        i = 0
        rst = 0
        while i < len(lst):
            print lst[i]
            rst = rst + lst[i]
            i += 2
        return rst