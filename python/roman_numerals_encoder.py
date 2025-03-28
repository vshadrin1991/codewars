'''
In Roman numerals:

1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.


Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''


def get_symbol(n):
    match(n):
        case 1000: return 'M'
        case 900: return 'CM'
        case 500: return 'D'
        case 400: return 'CD'
        case 100: return 'C'
        case 90: return 'XC'
        case 50: return 'L'
        case 40: return 'XL'
        case 10: return 'X'
        case 9: return 'IX'
        case 5: return 'V'
        case 4: return 'IV'
        case 1: return 'I'


def solution(val):
    data = [(get_symbol(i), val // i, val := val % i)
            for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]]
    return ''.join([d[0] * d[1] for d in data])


print(solution(4))
