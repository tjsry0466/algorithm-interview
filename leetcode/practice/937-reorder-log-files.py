from typing import List

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def reorder_log_files(logs: List[str]) -> List[str]:
    num = []
    str = []
    for log in logs:
        if log.split()[1].isdigit():
            num.append(log)
        else:
            str.append(log)
    
    str.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return str + num


print(reorder_log_files(logs))
