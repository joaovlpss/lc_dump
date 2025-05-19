from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min, max = 0, 0
        subtractions = [0]

        for idx in range(len(prices)):
            if prices[idx] < prices[min]:
                min = idx
                max = idx
                continue

            if prices[idx] > prices[max]:
                if idx > min:
                    subtractions.append(prices[idx] - prices[min])

                max = idx
                continue

        profit = 0
        for val in subtractions:
            if val > profit:
                profit = val

        return profit


mp1 = Solution().maxProfit([7, 6, 4, 3, 1])
print(mp1)
