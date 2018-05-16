class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = ["*"] + sorted(nums) +["*"]
        for i in range(1,len(lst)-1):
            if lst[i] != lst[i-1] and lst[i] != lst[i+1]:
                return lst[i]