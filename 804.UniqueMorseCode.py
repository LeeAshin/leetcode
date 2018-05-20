class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        M = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        C = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        dict = {}
        s = set()
        for i in range(0,26):
            dict[C[i]] = M[i]
        for word in words:
            rsl = ""
            for w in word:
                rsl = rsl + dict[w]
            s.add(rsl)
        return len(s)