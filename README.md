**Calories Predictor**

An application to predict the calories burned using inputs - Gender, Age, Height, Weight, Duraion and Heart rate (beats per minute). 
Multiple Machine and Deep Learning models were designed and the best performing model is used to predict the calories burned.

Python 3.8.12 - https://www.python.org/downloads/release/python-3812/

_Files description_ :
- data/calories.csv, data/exercise.csv - Dataset files used for models training. From https://www.kaggle.com/fmendes/fmendesdat263xdemos
- Wearables_data/apple_health_report- Apple health data to test models
- Model.ipynb - Machine and Deep learning models with data preparation and analysis
- app.py - Python file for the application (webpage)
- templates/home.html - Webpage design
- static/style.css - Webpage styling
- calorie_cal_run.py - Python script to automate package install, application hosting and webpage launch.

_Execution Steps_ :

calorie_cal_run.py will install packages. Execute the script in a virtual environment if required. 

1. Open command prompt or terminal
2. Navigate to the app root path using 'cd'
3. Execute command 'python calorie_cal_run.py '
Note : If the browser is launched and displays a message "Page not found" - please refresh the page once the application is successfully hosted in terminal.

Contributions :
1. Models design and Experimentation - Bhargavi Kallam, Rajitha Muthukrishnan
2. Webpage Design and Enhancement - Bhargavi Kallam, Rajitha Muthukrishnan
3. Model integration - Rajitha Muthukrishnan
4. Automated script (Package installation, Application execution, Webpage launch) - Bhargavi Kallam 

Github : https://github.com/Rajji7930/calorie_predictor.git
