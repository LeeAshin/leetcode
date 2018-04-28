class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_1 = set("qwertyuiop")
        keyboard_2 = set("asdfghjkl")
        keyboard_3 = set("zxcvbnm")

        result = []

        for word in words:
            word_l = set(word.lower())
            if word_l.issubset(keyboard_1) or word_l.issubset(keyboard_2) or word_l.issubset(keyboard_3):
                result.append(word)
            else:
                continue
        return result