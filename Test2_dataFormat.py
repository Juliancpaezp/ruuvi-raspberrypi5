from ruuvitag_sensor.ruuvi import RuuviTagSensor

def handle_data(found_data):
    data = found_data[1]
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

if __name__ == "__main__":
    RuuviTagSensor.get_data(handle_data)
