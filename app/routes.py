from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
import os
import csv
import json
import urllib



def countMalesAndFemales(persons):
    num_males = 0
    num_females = 0
    total_num = len(persons)

    for person in persons:
        gender = person[4].lower()
        if (gender == 'мужской' or gender == 'м'):
            num_males = num_males + 1 
        if (gender == 'женский' or gender == 'ж'):
            num_females = num_females + 1 

    percentage_males = num_males / total_num * 100
    percentage_females = num_females / total_num * 100

    return int(percentage_males), int(percentage_females)

def countAges(persons):
    total_of_group1 = 0
    total_of_group2 = 0
    total_of_group3 = 0
    total_of_group4 = 0

    for person in persons:
        person_age = int(person[3])
        if (person_age >= 18 and person_age <= 25):
            total_of_group1 = total_of_group1 + 1
        if (person_age > 25 and person_age <= 30):
            total_of_group2 = total_of_group2 + 1
        if (person_age >= 30 and person_age <= 35):
            total_of_group3 = total_of_group3 + 1
        if (person_age > 35):
            total_of_group4 = total_of_group4 + 1
    
    return total_of_group1, total_of_group2, total_of_group3, total_of_group4

def getNumOfClients(persons):
    return len(persons)

def getNumOfClientsByMonth(persons):
    num_in_january = 0
    num_in_february = 0
    num_in_march = 0
    num_in_april = 0
    num_in_may = 0
    num_in_june = 0
    num_in_july = 0
    num_in_august = 0
    num_in_september = 0
    num_in_october = 0
    num_in_november = 0
    num_in_december = 0

    for person in persons:
        month = person[10].split('.')[1] 
        if month == '01':
            num_in_january =  num_in_january + 1
        if month == '02':
            num_in_february =  num_in_february + 1
        if month == '03':
            num_in_march =  num_in_march + 1
        if month == '04':
            num_in_april =  num_in_april + 1
        if month == '05':
            num_in_may =  num_in_may + 1
        if month == '06':
            num_in_june =  num_in_june + 1
        if month == '07':
            num_in_july =  num_in_july + 1
        if month == '08':
            num_in_august =  num_in_august + 1
        if month == '09':
            num_in_september =  num_in_september + 1
        if month == '10':
            num_in_october =  num_in_october + 1
        if month == '11':
            num_in_november =  num_in_november + 1
        if month == '12':
            num_in_december =  num_in_december + 1
    
    return num_in_january, num_in_february, num_in_march, num_in_april, num_in_may, num_in_june, num_in_july, num_in_august, num_in_september, num_in_october,  num_in_november, num_in_december
        
def getProfitAndDamages(finances):

    profit_in_january = 0
    profit_in_february = 0
    profit_in_march = 0
    profit_in_april = 0
    profit_in_may = 0
    profit_in_june = 0
    profit_in_july = 0
    profit_in_august = 0
    profit_in_september = 0
    profit_in_october = 0
    profit_in_november = 0
    profit_in_december = 0

    damages_in_january = 0
    damages_in_february = 0
    damages_in_march = 0
    damages_in_april = 0
    damages_in_may = 0
    damages_in_june = 0
    damages_in_july = 0
    damages_in_august = 0
    damages_in_september = 0
    damages_in_october = 0
    damages_in_november = 0
    damages_in_december = 0


    for finance in finances:
        month = int(finance[0])
        profit_abonements = int(finance[2])
        profit_pool = int(finance[3])
        profit_box = int(finance[4])
        profit_trainee = int(finance[5])
        damages_equip = int(finance[6])
        damages_salary = int(finance[7])
        damages_qual = int(finance[8])
        damages_etc = int(finance[9])
    

        if (month == 1):
            profit_in_january = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_january = damages_equip + damages_salary + damages_qual + damages_etc
        if (month == 2):
            profit_in_february = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_february = damages_equip + damages_salary + damages_qual + damages_etc
        if (month == 3):
            profit_in_march = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_march = damages_equip + damages_salary + damages_qual + damages_etc
        if (month == 4):
            profit_in_april = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_april = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 5:
            profit_in_may = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_may = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 6:
            profit_in_june = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_june = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 7:
            profit_in_july = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_july = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 8:
            profit_in_august = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_august = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 9:
            profit_in_september = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_september = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 10:
            profit_in_october = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_october = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 11:
            profit_in_november = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_november = damages_equip + damages_salary + damages_qual + damages_etc
        if month == 12:
            profit_in_december = profit_abonements + profit_pool + profit_box + profit_trainee
            damages_in_december = damages_equip + damages_salary + damages_qual + damages_etc

    return profit_in_january, profit_in_february, profit_in_march, profit_in_april, profit_in_may, profit_in_june, profit_in_july, profit_in_august, profit_in_september, profit_in_october, profit_in_november, profit_in_december, damages_in_january, damages_in_february, damages_in_march, damages_in_april, damages_in_may, damages_in_june,damages_in_july, damages_in_august, damages_in_september, damages_in_october, damages_in_november, damages_in_december
        
    

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

        with open('AlexanderEx14\\AlexanderEx14_clients.csv', 'a', encoding="utf8") as f:
            f.write(",".join([surname, name, patronymic, age, sex, email, telephone, birth, subscription, price, purchase_date, end, soglasie]) + '\n')
            f.close()
        return render_template('clients_success.html', title="Клиент успешно добавлен")
    elif request.method == "GET":

        # Get data of clients from database
        with open('AlexanderEx14\\AlexanderEx14_clients.csv', newline='', encoding="utf8") as csvfile:
            clients_data = list(csv.reader(csvfile))

        cellData = json.dumps({'amount_of_clients': getNumOfClients(clients_data), 'new_clients_per_month': getNumOfClientsByMonth(clients_data)[0]})

        mfData = json.dumps({'male_percantage': countMalesAndFemales(clients_data)[0], 'female_percantage': countMalesAndFemales(clients_data)[1]})
        agesData = json.dumps({'group1': countAges(clients_data)[0], 'group2': countAges(clients_data)[1], 'group3': countAges(clients_data)[2], 'group4': countAges(clients_data)[3]})
        accumulateData = json.dumps({'Jan': getNumOfClientsByMonth(clients_data)[0], 'Feb': getNumOfClientsByMonth(clients_data)[1], 'Mar': getNumOfClientsByMonth(clients_data)[2], 'Apr': getNumOfClientsByMonth(clients_data)[3], 'May': getNumOfClientsByMonth(clients_data)[4], 'Jun': getNumOfClientsByMonth(clients_data)[5], 'Jul': getNumOfClientsByMonth(clients_data)[6], 'Aug': getNumOfClientsByMonth(clients_data)[7], 'Sep': getNumOfClientsByMonth(clients_data)[8], 'Oct': getNumOfClientsByMonth(clients_data)[9], 'Nov': getNumOfClientsByMonth(clients_data)[10], 'Dec': getNumOfClientsByMonth(clients_data)[11]})

        return render_template('clients.html', title='Клиенты', mfData=mfData, agesData=agesData, cellData=cellData, accumulateData=accumulateData)


@app.route('/finance', methods=['GET', 'POST'])
def finance():
    if request.method == 'POST':
        Month = request.form["Month"]
        Year = request.form["Year"]
        Income_from_the_sale_of_season_tickets = request.form["Income from the sale of season tickets"]
        Pool_service_income = request.form["Pool service income"]
        Income_from_the_service_group_boxing_lessons = request.form["Income from the service group boxing lessons"]
        Income_from_the_service_Individual_lessons_with_a_trainer = request.form["Income from the service Individual lessons with a trainer"]
        Equipment_maintenance_and_repair_costs = request.form["Equipment maintenance and repair costs"]
        Fitness_center_employee_salaries = request.form["Fitness center employee salaries"]
        Expenses_for_additional_training_courses_for_trainers = request.form["Expenses for additional training courses for trainers"]
        Other_expenses = request.form["Other expenses"]
        with open('AlexanderEx14\\AlexanderEx14_finances.csv', 'a', encoding="utf8") as f:
            f.write(",".join([Month,
                              Year,
                              Income_from_the_sale_of_season_tickets,
                              Pool_service_income,
                              Income_from_the_service_group_boxing_lessons,
                              Income_from_the_service_Individual_lessons_with_a_trainer,
                              Equipment_maintenance_and_repair_costs,
                              Fitness_center_employee_salaries,
                              Expenses_for_additional_training_courses_for_trainers,
                              Other_expenses]) + '\n')
            f.close()
        return render_template('finance_success.html', title='Финансы')
    elif request.method == "GET":

        #Get data of finances from database
        with open('AlexanderEx14\\AlexanderEx14_finances.csv', newline='', encoding="utf8") as csvfile:
            finance_data = list(csv.reader(csvfile))

        profitAndDamagesData = getProfitAndDamages(finance_data)

        profitData = json.dumps({'Jan': getProfitAndDamages(finance_data)[0], 'Feb': getProfitAndDamages(finance_data)[1], 'Mar': getProfitAndDamages(finance_data)[2], 'Apr': getProfitAndDamages(finance_data)[3], 'May': getProfitAndDamages(finance_data)[4], 'Jun': getProfitAndDamages(finance_data)[5], 'Jul': getProfitAndDamages(finance_data)[6], 'Aug': getProfitAndDamages(finance_data)[7], 'Sep': getProfitAndDamages(finance_data)[8], 'Oct': getProfitAndDamages(finance_data)[9], 'Nov': getProfitAndDamages(finance_data)[10], 'Dec': getProfitAndDamages(finance_data)[11]})
        damagesData = json.dumps({'Jan': getProfitAndDamages(finance_data)[12], 'Feb': getProfitAndDamages(finance_data)[13], 'Mar': getProfitAndDamages(finance_data)[14], 'Apr': getProfitAndDamages(finance_data)[15], 'May': getProfitAndDamages(finance_data)[16], 'Jun': getProfitAndDamages(finance_data)[17], 'Jul': getProfitAndDamages(finance_data)[18], 'Aug': getProfitAndDamages(finance_data)[19], 'Sep': getProfitAndDamages(finance_data)[20], 'Oct': getProfitAndDamages(finance_data)[21], 'Nov': getProfitAndDamages(finance_data)[22], 'Dec': getProfitAndDamages(finance_data)[23]})
    

        return render_template('finance.html', title='Финансы', profitData=profitData, damagesData=damagesData)

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