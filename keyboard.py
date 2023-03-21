import serial
import keyboard

arduino = serial.Serial('/dev/cu.usbmodem14101', 9600)

def on_press(key):

    if key.name == 'up':
        arduino.write(b'up\n')
    elif key.name == 'down':
        arduino.write(b'down\n')
    elif key.name == 'left':
        arduino.write(b'left\n')
    elif key.name == 'right':
        arduino.write(b'right\n')
    elif key.name == 'q':
        arduino.write(b'open\n')
    elif key.name == 'e':
        arduino.write(b'close')
keyboard.on_press(on_press)

while True:
    if keyboard.is_pressed('q'):
        break

arduino.close()