def replacer(str):
    match(str):
        case '(' | ')': return 1
        case '[' | ']': return 2
        case '{' | '}': return 3


def valid_braces(string):
    return [replacer(s) for s in string]


print(valid_braces("(){}[]"))
print(valid_braces("[({})](]"))
