import math


def rainbowcolor(i, full, reverse=False):
    if reverse:
        i = full - i
    if i < full / 3:
        r = 255
        g = math.ceil(255 * 3 * i / full)
        b = 0
    elif i < full / 2:
        r = math.ceil(750 - i * (250 * 6 / full))
        g = 255
        b = 0
    elif i < full * 2 / 3:
        r = 0
        g = 255
        b = math.ceil(i * (250 * 6 / full) - 750)
    elif i < full * 5 / 6:
        r = 0
        g = math.ceil(1250 - i * (250 * 6 / full))
        b = 255
    else:
        r = math.ceil(150 * i * (6 / full) - 750)
        g = 0
        b = 255
    return [r, g, b]

if __name__ == '__main__':
    print(rainbowcolor(0, 120, reverse=True))
