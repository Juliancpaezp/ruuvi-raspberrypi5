import matplotlib.pyplot as plt
import numpy as np
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from datetime import datetime
import pandas as pd

# Lists to store the data
measurement = []
temperatures = []
humidities = []
pressures = []
accelerations = []
battery_levels = []
rssi = []

# Initialize ploting
plt.ion()
fig = plt.figure()
plt.rcParams.update({'font.size': 6})


def handle_data(found_data):
    data = found_data[1]
    
    # Show data on console
    print("Received Data:")
    print(f"  MAC: {data['mac']}")
    print(f"  RSSI: {data['rssi']} dBm")
    print("  Environmental Data:")
    print(f"    Temperature: {data['temperature']} °C")
    print(f"    Humidity: {data['humidity']} %")
    print(f"    Pressure: {data['pressure']} hPa")
    print("  Motion Data:")
    print(f"    Acceleration (X): {data['acceleration_x']} m/s²")
    print(f"    Acceleration (Y): {data['acceleration_y']} m/s²")
    print(f"    Acceleration (Z): {data['acceleration_z']} m/s²")
    print("  Device Status:")
    print(f"    Tx Power: {data['tx_power']}")
    print(f"    Battery Level: {data['battery']} mV")
    print(f"    Movement Counter: {data['movement_counter']}")
    print(f"    Measurement Sequence Number: {data['measurement_sequence_number']}")
    print("\n")
    
    # Append measurement
    measurement.append(data.get('measurement_sequence_number'))
    # Append data to the respective lists
    temperatures.append(data.get('temperature'))
    humidities.append(data.get('humidity'))
    pressures.append(data.get('pressure'))
    # Calculate total acceleration from individual components
    acceleration = (data.get('acceleration_x')**2 + data.get('acceleration_y')**2 + data.get('acceleration_z')**2)**0.5
    accelerations.append(acceleration)
    # Append battery level
    battery_levels.append(data.get('battery'))
    # Append rssi
    rssi.append(data.get('rssi'))
    
    # Plotting
    
    # Temperature plot
    plt.subplot(2, 3, 1)
    plt.plot(measurement, temperatures, color='b', linewidth=2.0)
    plt.title('Temperature (°C)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Temperature')
    plt.grid(True)

    # Humidity plot
    plt.subplot(2, 3, 2)
    plt.plot(measurement, humidities, color='b')
    plt.title('Humidity (%)')
    #.xlabel('Data Point')
    #plt.ylabel('Humidity')
    plt.grid(True)

    # Pressure plot
    plt.subplot(2, 3, 3)
    plt.plot(measurement, pressures, color='b')
    plt.title('Pressure (hPa)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Pressure')
    plt.grid(True)

    # Acceleration plot
    plt.subplot(2, 3, 4)
    plt.plot(measurement, accelerations, color='b')
    plt.title('Acceleration (m/s²)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Acceleration')
    plt.grid(True)

    # Battery level plot
    plt.subplot(2, 3, 5)
    plt.plot(measurement, battery_levels, color='b')
    plt.title('Battery Level (mV)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Battery Level')
    plt.grid(True)
    
    # RSSI plot
    plt.subplot(2, 3, 6)
    plt.plot(measurement, rssi, color='b')
    plt.title('RSSI (dBm)')
    #plt.xlabel('Data Point')
    #plt.ylabel('RSSI')
    plt.grid(True)
    
    # DEBUG
    #print(measurement)

    # Cleaning plot for next iteration
    fig.set_size_inches(8, 5.5)
    fig.canvas.draw()
    fig.canvas.flush_events()


if __name__ == "__main__":
    
    RuuviTagSensor.get_data(handle_data)
    
