def connect_to():
    import network
    from time import sleep

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('Estableciendo conexión...')
        wlan.connect("Cooperadora Alumnos", "")
        while not wlan.isconnected():
            print(".", end="")
            sleep(0.5)

    print('Red conectada:', wlan.ifconfig())
    return wlan.ifconfig()[0]
