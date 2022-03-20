# Frøya | Froeya.  A weather app which gets local weather information from https://openweathermap.org/ ( WIP ).

## Setup  
To use this program, you need an account on openweathermap, aswell as an API key for the current weather API  https://openweathermap.org/current.  
To get API calls to work, make a file a file called config.ini within the src folder.  
#### Config.ini
[openweathermap]  
api=your_api_key_goes_here  

You will need Python3, pip and python pandas for this project.  
Refer to the proper documentation if need: https://flask.palletsprojects.com/en/2.0.x/  
Pythonpandas functionality is currently WIP.  

##Create and activate an enviorment

$ cd server/  
$ python3 -m venv venv  
$ . venv/bin/activate  

## Install Flask and dependencies

$ pip install Flask Flask-Session
$ flask run
