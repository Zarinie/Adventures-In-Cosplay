import time
import board
import neopixel

pixel_pin = board.D4
num_pixels = 51

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
CYAN = (0, 255, 255)

pixels.fill(CYAN)
pixels.show()
time.sleep(0.01)
