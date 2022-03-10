import os
import webbrowser
from sys import platform
from applescript import tell

if platform == "darwin" or platform == "linux":

    #os.system("""osascript -e 'tell application "Terminal" to do script "ls -l"'""")

    #set what command you want to run here
    Command_1 = 'cd path'
    tell.app( 'Terminal', 'do script "' + Command_1 + '"')

    Command_2 = 'pip install -r requirements.txt'
    tell.app( 'Terminal', 'do script "' + Command_2 + '"')

    Command_3 = 'python app.py'
    tell.app( 'Terminal', 'do script "' + Command_3 + '"')

    

else:
    #extracts the path of the specific file(i.e here calorie_count_run.py file)
    path = os.path.dirname(os.path.abspath(__file__))

    #opens the command promt and navigate to the path
    os.system("start cmd /c cd path" )

    #instals the requirements 
    os.system("start cmd /c pip install -r requirements.txt" )

    #atomatically runs app python file
    os.system("start cmd /k python app.py" )


#opens the website in the default browser
webbrowser.open('http://127.0.0.1:5000/')




