from typing import List


# 브루트포스
def two_sum1(nums: List[str], target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def two_sum2(nums: List[str], target: int):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 첫번째 수를 뺸 결과 키 조회
def two_sum3(nums: List[int], target: int) -> List[str]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        # 인덱스가 같지 않고 두번째 값이 키값에 있으면
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 조회 구조 개선
def two_sum4(nums: List[int], target: int) -> List[str]:
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 투 포인터 이동 (못품, 정렬되서 들어와야함)
def two_sum5(nums: List[int], target: int) -> List[int]:
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

print(two_sum1(nums, target))
print(two_sum2(nums, target))
print(two_sum3(nums, target))
print(two_sum4(nums, target))
print(two_sum5(nums, target))
