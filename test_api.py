import webbrowser
import time
import subprocess
import sys


# Start the Flask app
flask_process = subprocess.Popen([sys.executable, "app.py"])


# Wait for server to start
time.sleep(3)  

# Open the app in the browser
webbrowser.open("http://127.0.0.1:5000/predict")

