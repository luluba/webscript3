import os

class Config:
	KOGO_MAIL_SENDER='Mandy Liu <mandyliu0305@gmail.com>'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'wei lai zai wo men de shou shang!'
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG=True
	

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


