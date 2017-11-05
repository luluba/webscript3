class Config:
	KOGO_MAIL_SENDER='Mandy Liu <mandyliu0305@gmail.com>'

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


