import speech_recognition as sr
import serial

# create a recognizer instance
r = sr.Recognizer()
arduino = serial.Serial('/dev/cu.usbmodem14201', 9600)

# set the microphone as audio source
with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    # listen for audio input
    print("Ready for commands...")

    # continuously listen for commands
    while True:
        audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # try to recognize speech
            text = r.recognize_google(audio)
            print(text)
            int_ar = [int(substr) for substr in text.split('.')]

            # ensure each integer is within the valid range
            valid_int_ar = [max(0, min(255, i)) for i in int_ar]

            # convert to bytes and write to Arduino
            ar_bytes = bytes(valid_int_ar)
            arduino.write(ar_bytes)

        except sr.UnknownValueError:
            # speech was unintelligible
            print("Could not understand audio.")

