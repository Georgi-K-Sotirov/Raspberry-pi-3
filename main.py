from __future__ import absolute_import, division, print_function, \
    unicode_literals
import time
import scipy.io
import numpy as np

try:
    from ABElectronics_Python_Libraries.ADCDifferentialPi import ADCDifferentialPi
except ImportError:
    print("Failed to import ADCDifferentialPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys

        sys.path.append('..')
        from ADCDifferentialPi import ADCDifferentialPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


def main():
    # Initialize ADC object with the appropriate address and sample rate
    adc = ADCDifferentialPi(0x68, 0x69, 17)  # Set the sample rate to 17-bit resolution

    # Parameters for data collection
    num_samples = 1000  # Number of samples to collect
    sampling_interval = 1 / 3.75  # Sampling interval in seconds (3.75 SPS)

    # Initialize an empty list to store voltage readings
    voltage_readings = []

    try:
        for _ in range(num_samples):
            # Read voltage from channel 1
            voltage = adc.read_voltage(1)

            # Append voltage reading to the list
            voltage_readings.append(voltage)

            # Add a delay to control the sampling frequency
            time.sleep(sampling_interval)

        # Convert the list of voltage readings to a NumPy array
        voltage_array = np.array(voltage_readings)

        # Save the voltage data to a MATLAB file
        data = {'voltage': voltage_array}
        scipy.io.savemat('sinusoidal_data.mat', data)

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption gracefully
        print("\nData collection interrupted.")


if __name__ == "__main__":
    main()
