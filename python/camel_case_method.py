'''
Write a method (or function, depending on the language) that converts a string to camelCase, that is, 
all words must have their first letter capitalized and spaces must be removed.
'''


def camel_case(string: str) -> str:
    return ''.join([f'{s[:1].upper()}{s[1:]}' for s in string.split(' ')])


def camel_case_best(string: str) -> str:
    return string.title().replace(" ", "")


print(camel_case("test case"))
