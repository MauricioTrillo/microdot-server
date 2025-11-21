from boot import connect_to
from microdot import Microdot, send_file
from machine import Pin
import ds18x20
import onewire
import time

buzz = Pin(14, Pin.OUT)
sensor_pin = Pin(19)
ds = ds18x20.DS18X20(onewire.OneWire(sensor_pin))
temp_c = 0

connect_to()
app = Microdot()

@app.route('/')
async def home(request):
    return send_file('index.html')


@app.route('/<folder>/<filename>')
async def serve_static(request, folder, filename):
    return send_file(f"{folder}/{filename}")


@app.route('/sensors/ds18b20/read')
async def read_temperature(request):
    global temp_c
    ds.convert_temp()
    time.sleep_ms(750)

    rom_list = ds.scan()
    for rom in rom_list:
        temp_c = ds.read_temp(rom)

    return {'temperatura': temp_c}


@app.route('/setpoint/set/<int:set_val>')
async def handle_setpoint(request, set_val):
    global temp_c
    print("Procesando setpoint...")

    if set_val >= temp_c:
        buzz.on()
        state = {'buzzer': 'Encendido'}
    else:
        buzz.off()
        state = {'buzzer': 'Apagado'}

    return state


app.run(port=80)
