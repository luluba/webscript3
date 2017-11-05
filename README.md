# Webframe for KOGO 
web app for kogo

## Project Structure
```
|-webscript3  
  |-app/    
    |-templates/    
    |-static/    
    |-main/      
      |-__init__.py      
      |-errors.py      
      |-forms.py      
      |-views.py    
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
