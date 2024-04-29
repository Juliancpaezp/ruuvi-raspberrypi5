import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv #To save data on cvs file
import os  #To save on same folder as phyton script

from ruuvitag_sensor.ruuvi import RuuviTagSensor
from datetime import datetime #To add to file name

# Lists to store the data
measurements = []
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

# Create a "data" folder if it doesn't exist
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(data_folder, exist_ok=True)
# Generate a timestamp string
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# Create the CSV file path with the timestamp in the "data" folder
csv_file_path = os.path.join(data_folder, f'ruuvi_data_{timestamp}.csv')


def handle_data(found_data):
    data = found_data[1]
    
    ## Capture data
    MAC = data['mac']
    RSSI = data['rssi']
    temperature = data['temperature']
    humidity = data['humidity']
    pressure = data['pressure']/100 # hPa to Pascal
    accelX = data['acceleration_x'] * 9.81e-3 # mG to m/s3
    accelY = data['acceleration_y'] * 9.81e-3 # mG to m/s3
    accelZ = data['acceleration_z'] * 9.81e-3 # mG to m/s3
    tx_power = data['tx_power']
    battery = data['battery'] / 1000 # mV to V
    movement = data['movement_counter']
    measurement = data['measurement_sequence_number']
    
    ## Show data on console
    
    print("Received Data:")
    print(f"  MAC: {MAC}")
    print(f"  RSSI: {RSSI} dBm")
    print("  Environmental Data:")
    print(f"    Temperature: {temperature} °C")
    print(f"    Humidity: {humidity} %")
    print(f"    Pressure: {pressure} Pa")
    print("  Motion Data:")
    print(f"    Acceleration (X): {accelX} m/s²")
    print(f"    Acceleration (Y): {accelY} m/s²")
    print(f"    Acceleration (Z): {accelZ} m/s²")
    print("  Device Status:")
    print(f"    Tx Power: {tx_power}")
    print(f"    Battery Level: {battery} mV")
    print(f"    Movement Counter: {movement}")
    print(f"    Measurement Sequence Number: {measurement}")
    print("\n")
    
    ## Save data to .cvs file on same folder as script
    
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['MAC', 'RSSI', 'Temperature (°C)', 'Humidity (%)', 'Pressure (Pa)',
                      'Acceleration (X) (m/s²)', 'Acceleration (Y) (m/s²)', 'Acceleration (Z) (m/s²)',
                      'Tx Power', 'Battery (V)', 'Movement Counter', 'Measurement Sequence Number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'MAC': MAC,
                         'RSSI': RSSI,
                         'Temperature (°C)': temperature,
                         'Humidity (%)': humidity,
                         'Pressure (Pa)': pressure,
                         'Acceleration (X) (m/s²)': accelX,
                         'Acceleration (Y) (m/s²)': accelY,
                         'Acceleration (Z) (m/s²)': accelZ,
                         'Tx Power': tx_power,
                         'Battery (V)': battery,
                         'Movement Counter': movement,
                         'Measurement Sequence Number': measurement})
    
    ## Ploting data on real-time
    
    # Append measurement to lists
    measurements.append(measurement)
    # Append data to the respective lists
    temperatures.append(temperature)
    humidities.append(humidity)
    pressures.append(pressure)
    # Calculate total acceleration from individual components
    acceleration = (accelX**2 + accelY**2 + accelZ**2)**0.5
    accelerations.append(acceleration)
    # Append battery level
    battery_levels.append(battery)
    # Append rssi
    rssi.append(RSSI)
    
    # Temperature plot
    plt.subplot(2, 3, 1)
    plt.plot(temperatures, color='b', linewidth=2.0)
    plt.title(f'Current Temperature {temperature:.2f}  (°C)')
    #plt.xlabel('Data Point')
    plt.ylabel('Temperature')
    plt.grid(True)

    # Humidity plot
    plt.subplot(2, 3, 2)
    plt.plot(humidities, color='b')
    plt.title(f'Current Humidity {humidity:.2f} (%)')
    #.xlabel('Data Point')
    #plt.ylabel('Humidity')
    plt.grid(True)

    # Pressure plot
    plt.subplot(2, 3, 3)
    plt.plot(pressures, color='b')
    plt.title(f'Current Pressure {pressure:.2f} (Pa)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Pressure')
    plt.grid(True)

    # Acceleration plot
    plt.subplot(2, 3, 4)
    plt.plot(accelerations, color='b')
    plt.title(f'Current Acceleration {acceleration:.1f} (m/s²)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Acceleration')
    plt.grid(True)

    # Battery level plot
    plt.subplot(2, 3, 5)
    plt.plot(battery_levels, color='b')
    plt.title(f'Current Battery Level {battery:.1f} (V)')
    #plt.xlabel('Data Point')
    #plt.ylabel('Battery Level')
    plt.grid(True)
    
    # RSSI plot
    plt.subplot(2, 3, 6)
    plt.plot(rssi, color='b')
    plt.title(f'Current RSSI {RSSI} (dBm)')
    #plt.xlabel('Data Point')
    #plt.ylabel('RSSI')
    plt.grid(True)
    
    # DEBUG
    #print(rssi)

    # Cleaning plot for next iteration
    fig.set_size_inches(8, 5.5)
    fig.canvas.draw()
    fig.canvas.flush_events()


if __name__ == "__main__":
    
    RuuviTagSensor.get_data(handle_data)
    
