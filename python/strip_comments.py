'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.
'''


def strip_comments(strng: str, markers: list[str]):
    strings: list[str] = strng.split('\n')
    strings_data: list[tuple] = [(s, sorted([(s.index(m), m) for m in markers if m in s]))
                                 for s in strings]
    arr: list[str] = [str(sd[0]).split(sd[1][0][1])[0] if sd[1] else sd[0]
                      for sd in strings_data]
    return ('\n'.join([a.rstrip() if a != '' else a for a in arr]))


def best_solution(string, markers):
    parts = string.split('\n')
    for m in markers:
        parts = [v.split(m)[0].rstrip() for v in parts]
    return '\n'.join(parts)


print(strip_comments(
    "oranges bananas\napples\n@ ? .\n! - .\n# apples ?", ['-', '.', '#', ',', '=', '!', '?', '@', '^']))


print(best_solution(
    "oranges bananas\napples\n@ ? .\n! - .\n# apples ?", ['-', '.', '#', ',', '=', '!', '?', '@', '^']))
