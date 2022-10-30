import sys
from typing import List


# 브루트 포스로 계산
def max_profit(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# 현재값과 차이 계산
def max_profit1(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값으ㅡㄹ 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


nums = [7, 1, 5, 3, 6, 4]  # output: 5
print(max_profit(nums))
print(max_profit1(nums))
