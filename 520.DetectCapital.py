class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cword = word[0].upper()+ word[1:].lower()
        if word != word.lower() and word != word.upper() and word != cword:
            return False
        else:
            return True