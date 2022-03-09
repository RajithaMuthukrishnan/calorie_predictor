import os
import webbrowser

#extracts the path of the specific file(i.e here calorie_count_run.py file)
path = os.path.dirname(os.path.abspath(__file__))

#opens the command promt and navigate to the path
os.system("start cmd /c cd path" )

#instals the requirements 
os.system("start cmd /c pip install -r requirements.txt" )

#atomatically runs app python file
os.system("start cmd /c python app.py" )

#opens the website in the default browser
webbrowser.open('http://127.0.0.1:5000/')


