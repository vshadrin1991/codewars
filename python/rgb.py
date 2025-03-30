def rgb_gpt(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return "{:02X}{:02X}{:02X}".format(r, g, b)

print(rgb_gpt(-20, 275, 125))