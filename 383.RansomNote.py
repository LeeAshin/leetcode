class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rlist = list(ransomNote)
        mlist = list(magazine)
        try:
            for w in rlist:
                mlist.remove(w)
            return True
        except:
            return False