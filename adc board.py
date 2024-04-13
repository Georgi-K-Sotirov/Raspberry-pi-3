from ABElectronics_Python_Libraries.ADCDifferentialPi import ADCDifferentialPi
import time
import os

adc = ADCDifferentialPi(0x68, 0x69, 12)

# the conversion factor is the ratio of the voltage divider on the inputs
conversionfactor = 1.666
# setup these static values when the sensor is not moving
xStatic = 0
yStatic = 0
zStatic = 0
xMax = 0
xMin = 0
yMax = 0
yMin = 0
zMax = 0
zMin = 0


# get 50 samples from each ADC channel and use that to get an average value for 0G.
# Keep the accelerometer still while this part of the code is running
for x in range(0, 50):
    xStatic = xStatic + adc.read_voltage(1)
    yStatic = yStatic + adc.read_voltage(2)
    zStatic = zStatic + adc.read_voltage(3)
    xStatic = (xStatic / 50) * conversionfactor
    yStatic = (yStatic / 50) * conversionfactor
    zStatic = (zStatic / 50) * conversionfactor


while True:
    # read from adc channels and print to screen
    xVoltage =  (adc.read_voltage(1) * conversionfactor) - xStatic
    yVoltage = (adc.read_voltage(2) * conversionfactor) - yStatic
    zVoltage = (adc.read_voltage(3) * conversionfactor) - zStatic
    xForce = xVoltage / 0.3
    yForce = yVoltage / 0.3
    zForce = zVoltage / 0.3

    # Check values against max and min and update if needed
    if xForce >= xMax:
        xMax = xForce
    if xForce <= xMin:
        xMin = xForce
    if yForce >= yMax:
        yMax = yForce
    if yForce <= yMin:
        yMin = yForce
    if zForce >= zMax:
        zMax = zForce
    if zForce <= zMin:
        zMin = zForce

    # clear the console
    os.system('clear')

    # print values to screen
    print("X: %02f" % xForce)
    print("Y: %02f" % yForce)
    print("Z: %02f" % zForce)
    print("Max X: %02f" % xMax)
    print("Min X: %02f" % xMin)
    print("Max Y: %02f" % yMax)
    print("Min Y: %02f" % yMin)
    print("Max Z: %02f" % zMax)
    print("Min Z: %02f" % zMin)
    print("X Static Voltage: %02f" % xStatic)
    print("Y Static Voltage: %02f" % yStatic)
    print("Z Static Voltage: %02f" % zStatic)

    # wait 0.05 seconds before reading the pins again
    time.sleep(0.05)