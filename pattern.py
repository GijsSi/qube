import board
import time
import neopixel

pixels = neopixel.NeoPixel(board.D21, 125)

pattern = [[4],[3, 4, 5]] #data pin patronen
colour = [[0x190000], [0x190000 for x in range(3)]]
"""kleuren zijn hex en worden aangegeven met "0x".
Verder kan je "<kleur> for x in range(<lengte>)"
gebruiken om het patroon te vullen."""

while True:
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            pixels[pattern[i][j]] = colour[i][j]
        time.sleep(0.5)
        pixels.fill((0,0,0))

