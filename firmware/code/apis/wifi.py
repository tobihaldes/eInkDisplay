import network
import time

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # Aktivieren der WLAN-Schnittstelle

    # Verbindung zum WLAN-Netzwerk
    wlan.connect(ssid, password)

    # Warten auf die Verbindung
    timeout = 50  # Timeout nach 50 Sekunden
    while not wlan.isconnected() and wlan.status() >= 0 and timeout > 0:
        print("Waiting to connect...")
        time.sleep(5)
        timeout -= 10

    # Rückgabe des Verbindungsstatus
    if wlan.isconnected():
        print("Connected to the network")
        print(wlan.ifconfig())
        return True
    else:
        print("Failed to connect to the network")
        return False


# import network
# import time
# 
# # Initialisierung der WLAN-Schnittstelle
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)  # Aktivieren der WLAN-Schnittstelle
# 
# # Verbindung zum WLAN-Netzwerk
# wlan.connect('Notebook von Tobi', '1357924680')
# 
# # Warten auf die Verbindung
# while not wlan.isconnected() and wlan.status() >= 0:
#     print("Waiting to connect...")
#     time.sleep(10)
# 
# # Ausgabe der Netzwerkkonfiguration, wenn verbunden
# if wlan.isconnected():
#     print("Connected to the network")
#     print(wlan.ifconfig())
# else:
#     print("Failed to connect to the network")
# 


