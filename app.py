from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '2d627600da79d8cf0ac9af3d45cfc601da88e9f498e91cbe'

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
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
            messages.append({'fullName': fullName, 'amount': amount, 'paymentStatus': paymentStatus, 'date': date, 'remarks': remarks})
            return redirect(url_for('index'))
    
    return render_template('create.html')
