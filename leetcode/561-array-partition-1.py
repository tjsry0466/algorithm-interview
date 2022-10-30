from typing import List


# 정렬해서 맨 앞부터 2개씩 잘라서 최소값 더하면 만들수 있는 최소 페어중 최대값임.
def array_pair_sum1(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계싼
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


# 자리가 결정적이기 때문에 바로 구할 수 있음
def array_pair_sum2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum


# 파이선다운 방식
def array_pair_sum3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


nums = [1, 4, 3, 2]
print(array_pair_sum1(nums))  # 출력 4
print(array_pair_sum2(nums))  # 출력 4
print(array_pair_sum3(nums))  # 출력 4
