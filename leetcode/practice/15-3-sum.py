from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뚜기
        # i가 1 이상 되어야 이전 수가 존재함
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁하가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # 정답 처리
                results.append([nums[i], nums[left], nums[right]])

                # left의 다음수 중 똑같은 수가 있는 경우에 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # right의 이전수 중 똑같은 수가 있는 경우에 스킵
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


nums = [-1, 0, 1, 2, -1, -4]

print(three_sum(nums))
