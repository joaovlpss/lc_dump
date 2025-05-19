from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_l = int("999999")

        for s in strs:
            if len(s) < min_l:
                min_l = len(s)

        i = 0
        while i < min_l:
            for w in strs:
                if w[i] != strs[0][i]:
                    return w[:i]

            i += 1

        return s[:i]


sl = Solution()

print(sl.longestCommonPrefix(["flower", "flow", "flight"]))
