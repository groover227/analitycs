import os
import csv
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def catalog(self, username):
        dir_ = os.getcwd()  # Берется текущая рабочая директория
        return os.mkdir(os.path.join(dir_, username))

    def catalog_from_file(self, username):
        username = str(username)   #До этого не испольовал str
        dir_ = os.getcwd()  # Берется текущая рабочая директория
        return os.path.join(dir_, username)

    def file_name(self, username):
        username = str(username)
        file_username = username + '_' + 'clients' + '.csv'
        file_finance = username + '_' + 'finances' + '.csv'
        return file_username

    def files_(self, username, catalog):
        username = str(username)
        file_username = username + '_' + 'clients' + '.csv'
        file_finance = username + '_' + 'finances' + '.csv'

        users_information = [
            ['Фамилия', 'Имя', 'Отчество', 'Возраст', 'Пол', 'Email', 'Телефон', 'Дата рождения', 'Название абонемента', 'Цена абонемента', 'Дата приобретения абонемента', 'Дата истечения срока действия абонемента', 'Согласие на рассылку'],
        ]
        with open(os.path.join(catalog, file_username), "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(users_information)

        finance = [
            ['Доходы с продажи абонементов', 'Доходы с услуги "бассейн"', 'Доходы с услуги "групповые занятия боксом"', 'Доходы с услуги "Индивидуальные тренировки с тренером"', 'Расходы на содержание и починку оборудования', 'Расходы на заработную плату сотрудников фитнес-центра', 'Расходы на дополнительные курсы для повышения квалификации тренеров', 'Прочие расходы'],
        ]
        with open(os.path.join(catalog, file_finance), "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(finance)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
