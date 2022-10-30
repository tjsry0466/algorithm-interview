from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]
    print(out)

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= p
        p *= nums[i]

    return out


nums = [1, 2, 3, 4]
print(product_except_self(nums))
