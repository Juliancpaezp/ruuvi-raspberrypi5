import tkinter as tk
from ruuvitag_sensor.ruuvi import RuuviTagSensor

class RuuviSensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruuvi Sensor Data")

        self.temperature_label = tk.Label(root, text="Temperature:")
        self.temperature_label.pack()

        self.humidity_label = tk.Label(root, text="Humidity:")
        self.humidity_label.pack()

        self.pressure_label = tk.Label(root, text="Pressure:")
        self.pressure_label.pack()

        self.update_sensor_data()

    def update_sensor_data(self):
        try:
            # Assuming only one RuuviTag sensor is connected
            data = RuuviTagSensor.get_data_for_mac("cc:30:10:de:e9:af")
            temperature = data['temperature']
            humidity = data['humidity']
            pressure = data['pressure']

            self.temperature_label.config(text="Temperature: {:.2f} °C".format(temperature))
            self.humidity_label.config(text="Humidity: {:.2f} %".format(humidity))
            self.pressure_label.config(text="Pressure: {:.2f} hPa".format(pressure))

        except Exception as e:
            print("Error:", e)

        # Schedule the update after 1 second (1000 milliseconds)
        self.root.after(1000, self.update_sensor_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = RuuviSensorApp(root)
    root.mainloop()
