'''
Write a function named first_non_repeating_letter† that takes a string input, 
and returns the first character that is not repeated anywhere in the string.
'''


def first_non_repeating_letter(string: str) -> str:
    arr: list[str] = [
        s for s in string if string.lower().count(s.lower()) == 1]
    return "" if len(arr) == 0 else arr[0]


print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter(''))
