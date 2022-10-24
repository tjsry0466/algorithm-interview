import collections
import re
from typing import List


# 내 풀이
def most_common_word(s: str, banned: List[str]) -> str:
    arr = []
    for i in s.split():
        w = i.replace(".", "").replace(",", "").lower()
        if w not in banned:
            arr.append(w)

    counts = collections.Counter(arr)
    return counts.most_common(1)[0][0]


word = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_common_word(word, banned))


def most_common_word1(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]
