class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        List = []
        i = 0
        for fn in findNums:
            idx = nums.index(fn)
            if idx < len(nums)-1:
                for i in range(idx, len(nums)):
                    if nums[i] > fn:
                        List.append(nums[i])
                        break
                    else:
                        i += 1
                if i == len(nums):
                    List.append(-1)

            else:
                List.append(-1)
        return List