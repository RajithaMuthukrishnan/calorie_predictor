import os
import webbrowser


path = os.path.dirname(os.path.abspath(__file__))

os.system("start cmd /c cd path" )

os.system("start cmd /c pip install -r requirements.txt" )

os.system("start cmd /c python app.py" )

webbrowser.open('http://127.0.0.1:5000/')


