import network
import time

# Initialisierung der WLAN-Schnittstelle
wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # Aktivieren der WLAN-Schnittstelle

# Verbindung zum WLAN-Netzwerk
wlan.connect('Notebook von Tobi', '1357924680')

# Warten auf die Verbindung
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect...")
    time.sleep(10)

# Ausgabe der Netzwerkkonfiguration, wenn verbunden
if wlan.isconnected():
    print("Connected to the network")
    print(wlan.ifconfig())
else:
    print("Failed to connect to the network")
