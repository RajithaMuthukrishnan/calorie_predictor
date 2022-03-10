import os
import webbrowser

#extracts the path of the specific file(i.e here calorie_count_run.py file)
path = os.path.dirname(os.path.abspath(__file__))
# Install required packages
os.system('cd ' + path)
os.system('pip install -r requirements.txt')
# Host and launch the application
os.system('python app.py')
webbrowser.open('http://127.0.0.1:5000/')



