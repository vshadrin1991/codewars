
strarr: list[str] = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]
k: int = 2


def longest_consec(strarr: list[str], k: int) -> str:
    values: list[str] = [''.join(strarr[i:(i + k)])
                         for i in range(len(strarr)) if (i + k <= len(strarr))] if k > 0 else []
    return max(values, key=len) if len(values) > 0 else ''


print(longest_consec(strarr, k))
