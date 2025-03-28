def duplicate_count(text: str):
    lower_list: list[str] = [t.lower() for t in text]
    return len(set([l for l in lower_list if lower_list.count(l) > 1]))


def duplicate_count_short(text: str):
    return len(set([l for l in text.lower() if text.lower().count(l) > 1]))


print(duplicate_count('zN1vrdmsQhwyQeOLzUdccbd9'))
print(duplicate_count_short('zN1vrdmsQhwyQeOLzUdccbd9'))
