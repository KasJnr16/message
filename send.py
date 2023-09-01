import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected 
        Connected = True

    else:
        print("Connection failed")

Connected = False  # global variable for the state of the connection

client = mqtt.Client()
client.on_connect = on_connect
client.connect("2.tcp.eu.ngrok.io", 17913, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

join_name =input('Enter Join Name: ')
client.publish("glblcd", f'{join_name} JOINED!')

try:
    while True:
        name =input('Name: ')
        message = input('Your message: ')
        client.publish("glblcd", f'{name}: {message}')

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()