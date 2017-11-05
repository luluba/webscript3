# Web Framework for KOGO 
web app for kogo

## Project Structure
```
|-webscript3  
  |-app/    
    |-templates/    
    |-static/    
    |-main/      
      |-__init__.py  (application constructor)     
      |-errors.py      
      |-forms.py      
      |-views.py  (flask routes)  
    |-__init__.py    
    |-email.py    
    |-models.py  
 |-db/
 |-tests/    
   |-__init__.py  
   |-test*.py
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
