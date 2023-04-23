creat an virtual environment:
    python3 -m venv venv

activate the environment:
    source  venv/bin/activate

alternativ:
    pipenv shell
    pipenv install ...

install the Python Packages:
    pipenv install -r requiremtns.txt

create the .env an insert the 'weahter_key' in it:
    -> you can put this file (.env) into '.gitignore' so nobody can see your key

What i need for the OpenWeatherMap - API:
    latitude, longitude, appid

in 'app.py', make sure 'app.run()' debuge is set to false