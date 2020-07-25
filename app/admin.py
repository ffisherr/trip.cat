from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import flask_admin as admin

from app import app, db
from app.models import Trip, User, Organizer, Partner

admin = Admin(app, name='Панель администратора', template_mode='bootstrap3')

admin.add_view(ModelView(Trip, db.session, name='Путешествия'))
admin.add_view(ModelView(User, db.session, name='Пользователи'))
admin.add_view(ModelView(Organizer, db.session, name='Организаторы'))
admin.add_view(ModelView(Partner, db.session, name='Партнеры'))
