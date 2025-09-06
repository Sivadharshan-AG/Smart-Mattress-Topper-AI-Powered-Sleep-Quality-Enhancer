from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    sleep_stage = random.choice(["Awake", "Light Sleep", "Deep Sleep", "REM"])
    return render_template("index.html", stage=sleep_stage)

if __name__ == "__main__":
    app.run(debug=True)
