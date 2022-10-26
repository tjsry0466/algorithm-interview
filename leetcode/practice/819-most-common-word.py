import collections
import re
from typing import List


def most_common_word(paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()
    paragraph = re.sub('[^a-z0-9 ]', "", paragraph)
    paragraph = paragraph.split()
    dict = collections.defaultdict(int)

    print(paragraph)

    for word in paragraph:
        if word not in banned:
            dict[word] += 1
    print(dict)
    counters = collections.Counter(dict)
    return counters.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_common_word(paragraph, banned))
