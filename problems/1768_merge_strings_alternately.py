class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n_min = min(len(word1), len(word2))
        res = ""

        # we simply iterate through the shorter word, adding alternately
        for i in range(n_min):
            res += word1[i] + word2[i]

        # after that, we add all that's left of both words after the shorter word's length
        return res + word1[n_min:] + word2[n_min:]
