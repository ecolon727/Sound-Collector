# Credit to Isaac Wellish below for allowing this to be modified.
#Modified by Emmanuel Colon 

# The Perfect Pitch Machine
# By Isaac Wellish
# Creative Commons Licence (Anyone can use and hack the code, just give attributions please!)
#
# Big thanks to Adafruit!
# Much of this code was adapted from Adafruit's Circuit Playground Sound Meter tutorial found here:
# https://learn.adafruit.com/adafruit-circuit-playground-express/playground-sound-meter
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import audiobusio
import board
import array
import math
import time
import audioio
import neopixel


pixelBrightness = 0.05
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness= pixelBrightness)
NUM_SAMPLES = 160   #number to collect


#finds magnitude of input
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * NUM_SAMPLES)


# Root mean square (RMS)
# Remove DC bias before computing RMS.
def normalized_rms(values):
    minbuf = int(mean(values))
    return math.sqrt(sum(float((sample - minbuf) * (sample - minbuf)) for sample in values) / len(values))

def mean(values):
    return (sum(values) / len(values))
    

#input data to CSV
counter = 1
try:
    pixels[9] = (160,32,40)
    pixels.show()
    
    with open("/mag-data.csv", "a") as fp:
        while counter <= 20:          
            mic.record(samples, len(samples))
            magnitude = str(normalized_rms(samples))
            fp.write(magnitude + "\n")
            counter += 1
except OSError as e:
    print(e)
#End program