from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p *= nums[i]
    return out


nums = [1, 2, 3, 4]
# 출력 [24, 12, 8, 6]
print(product_except_self(nums))
