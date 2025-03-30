
# my design 
def maskify(cc: str):
    return ''.join([cc[::-1][i] if i < 4 else "#" for i in range(len(cc))])[::-1]

    
# best 
def maskify_best(cc : str): 
    return '#'*(len(cc[:-4])) + cc[-4:]


print(maskify("4556364607935616"))

print(maskify_best("4556364607935616"))