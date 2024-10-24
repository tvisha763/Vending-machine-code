import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

GPIO.setmode(GPIO.BCM)

reader = SimpleMFRC522()


def pay():

    try:
        _,  text = reader.read()

        with open("price.txt", "r") as file:
            price =  int(file.read())

        _,  text = reader.write(str(int(text)-price))

        with open("paid.txt", "w") as file:
            file.write("True")
            file.flush()

    finally:
        GPIO.cleanup()




def rotate(snack, steps , direction = 1):

    motor1 = [17, 18, 27, 22]
    motor2 = [23, 24, 25, 5]
    motor3 = [6, 12, 13, 19]
    motor4 = [26, 16, 20, 21]

    motors = [motor1, motor2, motor3, motor4]

    for motor in motors:
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    step_sequence = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    if snack == "kitkat":
        motor = motor1
    elif snack == "m&m":
        motor = motor2
    elif snack == "lays":
        motor = motor3
    else:
        motor = motor4

    try:
        for _ in range(steps):
            for step in step_sequence[::direction]:
                for pin in range(4):
                    GPIO.output(motor[pin], step[pin])
                time.sleep(0.002)
    except:
        pass
    finally:
        GPIO.cleanup()


