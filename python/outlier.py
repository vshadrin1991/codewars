def find_outlier(integers: list):
    return ([i for i in integers if i % 2 == 0] if len([i for i in integers if i % 2 != 0]) > 1 else [i for i in integers if i % 2 != 0])[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))