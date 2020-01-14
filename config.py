def ledConfig(width, length, height):
    pixels = [[[0 for z in range(height)] for y in range(length)] for x in range(width)]
    pixel = 0

    for x in range(len(pixels)):
        if x % 2 == 0:
            duck = range(len(pixels[x]))
        else:
            duck = range(len(pixels[x]) - 1, -1, -1)
        for y in duck:
            # if (x % 2 != 0 and y % 2 == 0) or (x % 2 == 0 and y % 2 != 0):
            #     duck = range(len(pixels[x][y])-1,-1,-1)
            # else:
            #     duck = range(len(pixels[x][y]))
            for z in range(len(pixels[x][y])):
                pixels[x][y][z] = pixel
                pixel += 1
    return pixels

def led_config2(x,y,z):
    # if (x % 2 != 0 and y % 2 == 0) or (x % 2 == 0 and y % 2 != 0):
    #     pixel = 49*x + 7*y - z + 6
    # elif (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
    if x % 2 == 0:
        pixel = 25*x + 5*y + z
    elif x % 2 != 0:
        pixel = 25*x + 5*y + z + 10
    return pixel



