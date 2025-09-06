import joblib
import serial

# Load model
model = joblib.load("sleep_model.pkl")

# Connect to Arduino
ser = serial.Serial("COM3", 9600)

while True:
    line = ser.readline().decode().strip()
    if "Pressure" in line:
        parts = line.replace("Pressure:", "").replace("Motion:", "").split(",")
        pressure, motion = int(parts[0]), int(parts[1])
        heart_rate = 70  # placeholder value or from sensor

        prediction = model.predict([[pressure, motion, heart_rate]])
        print("Predicted Sleep Stage:", prediction[0])
