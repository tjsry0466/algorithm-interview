# 에너그램이란.
# 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.
import collections
from typing import List

inputArr = ["eat", "tea", "tan", "ate", "nat", "bat"]


def sort_anagrams(strs: List[str]) -> List[List[str]]:
    # collections.defaultdict로 자료형을 넘기면 기본값을 설정해줌
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


print(sort_anagrams(inputArr))
