from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range) 
pixel_used = 16
program_state = "DIMM"
loop_range = None

button_pin = Pin(39, Pin.IN)  # configure input on pin G39 (atom matrix display button)
system_on = False
button_low_prev = 1

neopixel_pin = Pin(23, Pin.OUT)  # configure output on pin G27 (atom matrix display)
neopixel_strip = NeoPixel(neopixel_pin, pixel_used)  # create NeoPixel object with 25 pixels

rainbow = [
  (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
  (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
  (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
  (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

while True:
    # read 12-bit analog value (0 - 4095 range)
    analog_val = adc.read()  
    # print to terminal
    print(analog_val)
    # Clear out the strip at the beginning
    for i in range(pixel_used):
        neopixel_strip[i] = (0,0,0)
    # Convert range
    loop_range = map_value(analog_val,700,2100,0,pixel_used)

    if system_on:
        rainbow = rainbow[-1:] + rainbow[:-1]
        for i in range(loop_range):
            neopixel_strip[i] = rainbow[i]

        neopixel_strip.write()  # write color data to neopixels
    else:
        neopixel_strip.write()
    
    # button_pin is low and last time button_pin was not on
    if button_pin.value() == 0 and button_low_prev != 0:  
        system_on = not system_on

    button_low_prev = button_pin.value()
    sleep_ms(100)



        # analog_val_8bit = map_value(analog_val, in_min = 0, in_max = 4095, out_min = 0, out_max = 255)
        #print(analog_val)
        #print(analog_val_8bit)
        # changing how many neopixels are colored using ADC value:
        # map ADC value from 0 - 4095 range to 0 - 30
        # analog_val_25 = map_value(analog_val, 0, 4095, out_min = 0, out_max = 25)
        # print(analog_val_25)

        # if(analog_val > 1000):