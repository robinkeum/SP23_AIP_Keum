# Final documentation
## Smart Home system


Project Summary

This project is a smart home system mockup using different sensors for input and led light as an output

It's a creative light experience for the house model, using different system states. When the button is pressed to turn on the system, light sensor detects the brightness level near by through the roof window, and if it is bright the led light system of the house gets dimmer and if the surrounding is dark it gets brighter, automatically controlling the lighting environment.

When the button is pressed for the second time, the system mode changes to home security mode where it checks if there are anything in the house using PIR sensor, and if the sensor detection is true, the light turns on to be bright red color with can be visible from even outside the house model and an email gets sent using IFTTT and webhooks to alert the user that there was a movement detected in the house.

## Implementation

Using Atom matrix and PIR sensor, light sensor, this project shows the output using led light strip. Physical Model shows a modern house to demonstrate how this system is supposed to be used as a home lighting system.


## Hardware

* Breadboard
* Atom Matrix
* Wires
* PIR sensor
* Light Sensor


## Firmware


```

# pir motion
pir_sensor_IN = Pin(33, Pin.IN)   # configure input on pin G33 (white wire)
# light output
neopixel_pin = Pin(25, Pin.OUT)  # configure output on pin G25 (neopixel strip)
neopixel_strip = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels
# change arguments below to connect to the WiFi network, such as 'ACCD':
wifiCfg.doConnect('ACCD', 'tink1930')  

button_IN = Pin(23, Pin.IN)  # configure input on pin G32 (atom matrix display button)
system_mode = 0
button_low_prev = 1
is_email_sent = False
send_email = False

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire) for analog sensor (light)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

```

## Software

Used IFTTT and webhooks to send email once PIR sensor detects movement

'''

if system_mode == 2:
        print("PIR: " + str(pir_sensor_val))
        if (send_email == True and not is_email_sent):
            # WEBHOOK
            try:
            # post http request to ifttt:
                req = urequests.request(method='POST', url='http://maker.ifttt.com/trigger/PIR_Sensor/with/key/dhVpcfxqcUTIqTZXa1Sn6R',json={'value_name':'value'}, headers={'Content-Type':'application/json'})
                print('success!')
                is_email_sent = True
                send_email = False
            except:
                print('fail..')
            sleep_ms(500)
            
'''

## Integrations

Include a link to and/or screenshots of other functional components of your project, like Adafruit IO feeds, dashboards, IFTTT applets, etc. In general, think of your audience as someone new trying to learn how to make your project and make sure to cover anything helpful to explain the functional parts of it.

## Enclosure / Mechanical Design

Explain how you made the enclosure or any other physical or mechanical aspects of your project with photos, screenshots of relevant files such as laser-cut patterns, 3D models, etc. (it’s great if you’re willing to share the editable source files too!)

## Project outcome

It's a creative light experience for the house model, using different system states. When the button is pressed to turn on the system, light sensor detects the brightness level near by through the roof window, and if it is bright the led light system of the house gets dimmer and if the surrounding is dark it gets brighter, automatically controlling the lighting environment.

When the button is pressed for the second time, the system mode changes to home security mode where it checks if there are anything in the house using PIR sensor, and if the sensor detection is true, the light turns on to be bright red color with can be visible from even outside the house model and an email gets sent using IFTTT and webhooks to alert the user that there was a movement detected in the house.

## Video Documentation
 Video can be found in google drive 
 [drive](https://drive.google.com/drive/folders/1dVsFapkpwBK-gSAbKA4YA6HCj-IvOEPN?usp=sharing)
 
## Conclusion

This project was a combination of every small projects I worked on through this entire term. Starting with the security system using led lights with the creative button challenge. Midterm lighting system also helped me bring this final project to life by getting the practice using led strip as an output. The final system works as a smart lighting system for the house and I am very happy at the fact that all of the skills I learned throught this entire term was put to use and without too much of technical difficulty, was able to show a demo during the presentation. IFTTT and webhooks email was challenging but the overall project turned out great.
