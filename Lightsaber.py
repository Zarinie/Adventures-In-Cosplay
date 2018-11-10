import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D4
num_pixels = 51
is_color_up = False

def color_up(color, wait):
    global is_color_up
    if not is_color_up:
        j = 50
        for i in range(25):
            pixels[i] = color
            pixels[j] = color
            time.sleep(wait)
            pixels.show()
            j= j - 1
        pixels[25] = color
        pixels.show()
        is_color_up = True
        #time.sleep(0.5)

def color_down(color, wait):
    global is_color_up
    if is_color_up:
        j = 0
        k = 50
        for i in range(25+1):
            pixels[k] = color
            pixels[j] = color
            time.sleep(wait)
            pixels.show()
            j = j + 1
            k = k -1
        is_color_up = False
        #pixels[25] = color
        #time.sleep(0.5)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
#for i in range(num_pixels):
#    pixels[i] = OFF
pixels.show()
CYAN = (0, 255, 255)
RED = (255, 0, 0)
OFF = (0,0,0)

switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

#pixels.fill(CYAN)
#pixels.show()
#time.sleep(0.01)

#color_up(CYAN, 0.01)
#color_down(OFF, 0.01)
#sleep(0.3)

while True:
    if switch.value:
        color_down(OFF, 0.01)
        #pixels.setBrightness(0.01)
        #pixels.fill(OFF)
        #pixels.show()
        #print("off")
    else:
        #pixels.setBrightness(0.3)
        color_up(CYAN, 0.01)
        #pixels.fill(CYAN)
        #pixels.show()
        #print("on")
    time.sleep(0.01)
