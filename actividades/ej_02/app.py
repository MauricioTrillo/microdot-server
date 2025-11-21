from microdot import Microdot, send_file
from machine import Pin
from boot import connect_to
import neopixel
import network
from time import sleep

led_1 = Pin(32, Pin.OUT, value=0)
led_2 = Pin(33, Pin.OUT, value=0)
led_3 = Pin(25, Pin.OUT, value=0)

rgb_strip = neopixel.NeoPixel(Pin(27), 4)
for idx in range(4):
    rgb_strip[idx] = (0, 0, 0)
rgb_strip.write()

connect_to()

app = Microdot()


@app.route('/')
async def home(request):
    return send_file('index.html')


@app.route('/<folder>/<filename>')
async def serve_static(request, folder, filename):
    return send_file("/{}/{}".format(folder, filename))


@app.route('/led/toggle/<led_name>')
async def toggle_led(request, led_name):
    global led_1, led_2, led_3

    if led_name == 'LED1':
        led_1.value(not led_1.value())
    elif led_name == 'LED2':
        led_2.value(not led_2.value())
    elif led_name == 'LED3':
        led_3.value(not led_3.value())

    return {"status": "OK"}


@app.route('/rgbled/change/<int:r>/<int:g>/<int:b>')
async def update_rgb(request, r, g, b):
    global rgb_strip

    for p in range(4):
        rgb_strip[p] = (r, g, b)
    rgb_strip.write()

    return {"status": "OK"}


app.run(port=80)
