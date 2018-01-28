import os

class Config:
	KOGO_MAIL_SENDER='Mandy Liu <mandyliu0305@gmail.com>'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'wei lai zai wo men de shou shang!'
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG=True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'mysql://root:password@localhost/shopit'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True #automatic commits of db changes
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
class TestingConfig(Config):
	TESTING=True

class ProductionConfig(Config):
	pass

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,	
	
	'default': DevelopmentConfig
}	


