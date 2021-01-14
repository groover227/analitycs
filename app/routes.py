from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
import os


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        user.catalog(username=form.username.data)
        catalog_from_file = user.catalog_from_file(username=form.username.data)
        user.files_(username=form.username.data, catalog=catalog_from_file)
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/clients', methods=['GET', 'POST'])
def writeClients():
    if request.method == 'POST':
        surname = request.form["surname"]
        name = request.form["name"]
        patronymic = request.form["patronymic"]
        age = request.form["age"]
        sex = request.form["sex"]
        email = request.form["email"]
        telephone = request.form["telephone number"]
        birth = request.form["data of birth"]
        subscription = request.form["subscription name"]
        price = request.form["subscription price"]
        purchase_date = request.form["Subscription purchase date"]
        end = request.form["Expiration date of the subscription"]
        soglasie = request.form["Expiration date of the subscription"]

        with open('AlexanderEx13_clients.csv', 'a') as f:
            f.write(",".join([surname, name, patronymic, age, sex, email, telephone, birth, subscription, price, purchase_date, end, soglasie]) + '\n')
            f.close()
        return "Информация о новом клиенте добавлена!"
    elif request.method == "GET":
        return render_template('clients.html', title='Клиенты')


@app.route('/finance', methods=['GET', 'POST'])
def finance():
    if request.method == 'POST':
        Income_from_the_sale_of_season_tickets = request.form["Income from the sale of season tickets"]
        Pool_service_income = request.form["Pool service income"]
        Income_from_the_service_group_boxing_lessons = request.form["Income from the service group boxing lessons"]
        Income_from_the_service_Individual_lessons_with_a_trainer = request.form["Income from the service Individual lessons with a trainer"]
        Equipment_maintenance_and_repair_costs = request.form["Equipment maintenance and repair costs"]
        Fitness_center_employee_salaries = request.form["Fitness center employee salaries"]
        Expenses_for_additional_training_courses_for_trainers = request.form["Expenses for additional training courses for trainers"]
        Other_expenses = request.form["Other expenses"]
        with open('AlexanderEx13_finances.csv', 'a') as f:
            f.write(",".join([Income_from_the_sale_of_season_tickets, Pool_service_income, Income_from_the_service_group_boxing_lessons, Income_from_the_service_Individual_lessons_with_a_trainer, Equipment_maintenance_and_repair_costs, Fitness_center_employee_salaries, Expenses_for_additional_training_courses_for_trainers, Other_expenses]) + '\n')
            f.close()
        return "Информация о финансах добавлена!"
    elif request.method == "GET":
        return render_template('finance.html', title='Финансы')

@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    return render_template('workouts.html', title='Тренировки')

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    return render_template('membership.html', title='Абонементы')

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    return render_template('attendance.html', title='Посещаемость')

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    return render_template('staff.html', title='Персонал')

@app.route('/timetable', methods=['GET', 'POST'])
def timetable():
    return render_template('timetable.html', title='Расписание')

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    return render_template('reports.html', title='Отчёты')