class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count += 1
                nums[i] = ""
        while '' in nums:
            nums.remove('')
        for x in range(0, count):
            nums.append(0)


"""
class Solution(object): 
    def swap(self, nums, i, j): 
        temp = nums[j] 
        nums[j] = nums[i] 
        nums[i] = temp 
    def moveZeroes(self, nums): 

 
        length = len(nums)
        nums[:] = [x for x in nums if x != 0]
        nums.extend([0] * (length - len(nums)))
        """