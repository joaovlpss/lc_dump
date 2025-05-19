class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        combos = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        res = 0

        # first we count all combos and remove them from the number 
        for combo in combos:
            if combo in s:
                s = s.replace(combo, "")
                res += combos[combo]

        # then we count the rest
        for num in s:
            res += mapping[num]

        return res

solution = Solution()

print(solution.romanToInt("MCMXCIV"))