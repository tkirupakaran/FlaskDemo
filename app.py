from tkinter import messagebox

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from tkinter import *

from main import msgbox, CreateRndmNum

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="1234qwer$"
app.config["MYSQL_DB"]="pydb"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql= MySQL(app)



@app.route('/')
def home():
    return render_template('MainPage.html')

@app.route('/UserCreation', methods=['GET','POST'])
def UserCreation():
    if request.method == 'POST':
        global fn, ln, age, add1, c, st, pin
        fn = request.form.get('fname')
        ln = request.form.get('lname')
        age = request.form.get('age')
        add1 = request.form.get('add1')
        c = request.form.get('City')
        st = request.form.get('state')
        pin = request.form.get('pincode')

        #return render_template('ConfirmPage.html', firstName=fn, lastName=ln, age=age, address=add1, city=c, state=st, pinCode=pin)
        #return redirect('ConfirmPage.html', firstName=fn, lastName=ln, age=age, address=add1, city=c, state=st, pinCode=pin)
        return redirect(url_for('ConfirmPage'))

        ##return render_template('ConfirmPage.html', firstName=fn, lastName=ln, age=age, address=add1, city=c, state=st, pinCode=pin)


    return render_template('UserCreation.html')

@app.route("/ConfirmPage", methods=['GET', 'POST'])
def ConfirmPage():
    if request.method == 'POST':

        #return render_template('ConfirmPage.html', firstName=fn, lastName=ln, age=age, address=add1, city=c, state=st, pinCode=pin)
        accNum = CreateRndmNum()
        msgbox(accNum)
        conn = mysql.connection.cursor()
        sqlQ = "insert into users (FirstName,LastName,Age,Address,City,State,Pin,AccountNumber) value (%s, %s, %s, %s, %s, %s, %s, %s)"

        conn.execute(sqlQ, [fn, ln, age, add1, c, st, pin, accNum])
        mysql.connection.commit()
        conn.close()
        return render_template('MainPage.html')
    return render_template('ConfirmPage.html', firstName=fn, lastName=ln, age=age, address=add1, city=c, state=st, pinCode=pin)
'''
        # to fetch and insert the data in to the DB
        fn = request.form.get('fname')
        ln = request.form.get('lname')
        age = request.form.get('age')
        add1 = request.form.get('add1')
        c = request.form.get('City')
        st = request.form.get('state')
        pin = request.form.get('pincode')
  
'''




@app.route('/FundTransfer')
def FundTransfer():
    return "<h1>Fund Transfer</h1>"

@app.route('/ViewStatement')
def ViewStatement():
    return "<h1>View Statement</h1>"


if __name__ == "__main__":
    app.run(debug=True)


