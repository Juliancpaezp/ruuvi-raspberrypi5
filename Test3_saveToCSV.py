import csv #To save data on cvs file
import os  #To save on same folder as phyton script
from datetime import datetime #To add to file name

from ruuvitag_sensor.ruuvi import RuuviTagSensor

# Create a "data" folder if it doesn't exist
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(data_folder, exist_ok=True)
# Generate a timestamp string
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# Create the CSV file path with the timestamp in the "data" folder
csv_file_path = os.path.join(data_folder, f'ruuvi_data_{timestamp}.csv')


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
    
    # Save data to .cvs file on same folder as script
    #current_directory = os.path.dirname(os.path.abspath(__file__))
    #csv_file_path = os.path.join(data_folder, 'ruuvi_data.csv')
    
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['MAC', 'RSSI', 'Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)',
                      'Acceleration (X) (m/s²)', 'Acceleration (Y) (m/s²)', 'Acceleration (Z) (m/s²)',
                      'Tx Power', 'Battery (mV)', 'Movement Counter', 'Measurement Sequence Number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'MAC': data['mac'],
                         'RSSI': data['rssi'],
                         'Temperature (°C)': data['temperature'],
                         'Humidity (%)': data['humidity'],
                         'Pressure (hPa)': data['pressure'],
                         'Acceleration (X) (m/s²)': data['acceleration_x'],
                         'Acceleration (Y) (m/s²)': data['acceleration_y'],
                         'Acceleration (Z) (m/s²)': data['acceleration_z'],
                         'Tx Power': data['tx_power'],
                         'Battery (mV)': data['battery'],
                         'Movement Counter': data['movement_counter'],
                         'Measurement Sequence Number': data['measurement_sequence_number']})

if __name__ == "__main__":
    RuuviTagSensor.get_data(handle_data)
