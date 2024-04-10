import tkinter as tk

import RPi.GPIO as GPIO

# Declare global variables
pwm = None

# Pin definitions
led_pin = 12

# This gets called whenever the scale is changed--change brightness of LED
def dim(i):

    global pwm

    # Change the duty cycle based on the slider value
    pwm.ChangeDutyCycle(float(i))

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Initialize pwm object with 50 Hz and 0% duty cycle
pwm = GPIO.PWM(led_pin, 50)
pwm.start(0)

# Create the main window and set initial size
root = tk.Tk()
root.title("LED Dimmer")
root.geometry("150x300")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container (center it in the window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create scale widget
scale = tk.Scale(   frame,
                    orient=tk.VERTICAL,
                    from_=100,
                    to=0,
                    length=200,
                    width=50,
                    sliderlength=50,
                    showvalue=False,
                    command=dim )

# Lay out widget in frame
scale.pack()

# Run forever!
root.mainloop()

# Stop, cleanup, and exit when window is closed
pwm.stop()
GPIO.cleanup()
