class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split(" ")
        while '' in word:
            word.remove('')
        if len(word) != 0:
            return len(word[-1])
        else:
            return 0