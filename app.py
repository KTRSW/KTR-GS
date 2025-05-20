import os
from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    reason = request.form['reason']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, name, email, reason])

    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return '신청이 완료되었습니다. 감사합니다!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
