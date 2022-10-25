# 두 요소를 더하여 특정 값이 나오는 인덱스를 찾는 문제
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def two_sum1(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 첫번째 수를 뺀 결과 키 조회
def two_sum2(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    # nums_map = {2: 0, 7: 1, 11: 2, 15: 3}

    # 타겟에서 첫 번째 수를 뺸 결과를 키로 조회
    for i, num in enumerate(nums):
        # 값으로 키를 조회함, 해당 값이 있으면 해당 인덱스가 곧 두번째 index
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


def two_sum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# nums는 정렬되있지 않아 해당 방법으로 풀수 없음 X
def two_sum4(nums: List[int], target: int) -> List[int]:
    nums.sort()  # 정렬하면 순서가 엉망이 되어버려 문제를 풀 수 없다.

    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
print(two_sum1(nums, target))
print(two_sum2(nums, target))
print(two_sum3(nums, target))
print(two_sum4(nums, target))
