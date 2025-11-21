def connect_to():
    import network
    from time import sleep

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    if not wifi.isconnected():
        print('Iniciando conexión WiFi...')
        wifi.connect("Cooperadora Alumnos", "")
        while not wifi.isconnected():
            print(".", end="")
            sleep(0.5)

    print('Red configurada:', wifi.ifconfig())
    return wifi.ifconfig()[0]
