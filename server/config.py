import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = 'dlkvmdflkmvldfmvklkdvmlkvmdlkvlkdmfvlkdfmvl'
	SQLALCHEMY_DATABASE_URI 	   = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_MIGRATE_REPO        = os.path.join(basedir, 'db_repository')
	SQLALCHEMY_COMMIT_ON_TEARDOWN  = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	FLASK_ADMIN_SWATCH = 'cerulean'
