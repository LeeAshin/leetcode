class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = ""
        q = []
        for num in nums:
            seq += str(num)
        rsl = seq.split("0")
        for l in rsl:
            q.append(len(l))
        return max(q)