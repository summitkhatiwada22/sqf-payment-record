from flask import Flask, render_template, request, url_for, flash, redirect
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '2d627600da79d8cf0ac9af3d45cfc601da88e9f498e91cbe'
messages = []
with open('db.json', 'r') as f:
    messages = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    global messages
    if request.method == 'POST':
        fullName = request.form['fullName']
        amount = request.form['amount']
        paymentStatus = request.form['paymentStatus']
        date = request.form['date']
        remarks = request.form['remarks']

        if not fullName:
            flash('Vendor Name is required!')
        elif not amount:
            flash('Amount is required!')
        elif not paymentStatus:
            flash('Payment Status is required!')
        elif not date:
            flash('Date is required!')
        elif not remarks:
            flash('Remarks is required!')
        else:
            with open('db.json', 'w') as file:
                # messages = json.load(file)
                messages.append({'fullName': fullName, 'amount': amount, 'paymentStatus': paymentStatus, 'date': date, 'remarks': remarks})
                # file.seek(0)
                json.dump(messages, file)
            return redirect(url_for('index'))
    
    return render_template('create.html')
