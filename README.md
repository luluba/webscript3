# Web Framework for KOGO 
web app for kogo

## Project Structure
```
|-webscript3  
  |-app/    
    |-templates/    
    |-static/    
    |-main/      
      |-__init__.py  (main blueprint)     
      |-errors.py      
      |-forms.py      
      |-views.py  (flask routes)  
    |-auth/
      |-__init__.py (auth blueprint)
      |-views.py (the authorization views using oauth 2.0)
    |-__init__.py (application constructor)  
    |-models.py ( sqlalchemy )
 |-db/
 |-tests/    
   |-__init__.py  
 |-venv/  
 |-requirements.txt  
 |-config.py  
 |-manage.py
```
* app: Flask application
* db: database scripts
* tests: unit tests
* venv.py: python virtual environment
* requirement.txt: all the package dependencies to regenerate the same virtual environment
* config.py: configuration settings
* manage.py: launch the application and other tasks.

## Generate Python Virtual Environment:
* Create the python virtual environment
```
pip install virtualenv
cd webscript3
virtualenv venv
```

* Activate the virtual environment
```
source venv/bin/activate
```
* Replicate the virtual environment
```
pip install -r requirements.txt
```
* Update the virtual environment
```
pip freeze >requirements.txt
git commit
```
## OAuth 2.0
* [Credentials page]: Create authorization credentials
```
For testing, URIS: http://localhost:5000
for redirect URIs: http://localhost:5000/oauth2callback
```
* Download client_secret.json file and store the file in a safe location


[Credentials page]: https://console.developers.google.com/apis/credentials
