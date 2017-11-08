#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
