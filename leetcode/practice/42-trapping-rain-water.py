from typing import List


def trapping_rain_water(arr: List[int]) -> int:
    if not arr:
        return 0

    volume = 0
    left, right = 0, len(arr) - 1
    left_max, right_max = arr[left], arr[right]

    while left < right:
        left_max, right_max = max(arr[left], left_max), max(arr[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - arr[left]
            left += 1
        else:
            volume += right_max - arr[right]
            right -= 1

    return volume


def trapping_rain_water_stack(arr: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(arr)):
        # 변곡점을 만나는 경우
        # arr[i]는 현재 위치, arr[stack[-1]]은 가장 최근에 스택에 넣은 것(가장 최근 위치?)
        while stack and arr[i] > arr[stack[-1]]:
            print(arr[stack[-1]], arr[i])
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(arr[i], arr[stack[-1]]) - arr[top]

            volume += distance * waters

        stack.append(i)
    return volume


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapping_rain_water(arr))
print(trapping_rain_water_stack(arr))
