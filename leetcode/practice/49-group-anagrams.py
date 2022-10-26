import collections
from typing import List

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(arr: List[str]) -> List[List[str]]:
    dict = collections.defaultdict(list)

    for i in arr:
        dict[''.join(sorted(i))].append(i)
    print(dict)
    return list(dict.values())


print(group_anagrams(arr))
