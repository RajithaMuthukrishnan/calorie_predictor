import os
import subprocess
import webbrowser
import time
from threading import Thread

# extracts the path of the specific file(i.e here calorie_count_run.py file)
path = os.path.dirname(os.path.abspath(__file__))
# Install required packages
os.system('cd ' + path)
os.system('pip install -r requirements.txt')
# Host and launch the application
def serve_command():
    os.system('python app.py')
program = Thread(target=serve_command)
program.start()
time.sleep(5)

webbrowser.get().open('http://localhost:5000/')

