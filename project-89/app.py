from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/getweather', methods=['POST'])
def calculate():
    if request.method == 'POST' and 'dt1' in request.form and 'dt2' in request.form:
        
        dt1 = int(request.form.get('dt1'))
        dt2 = int(request.form.get('dt2'))
        m1 = int(request.form.get('m1'))
        m2 = int(request.form.get('m2'))
        year1 = int(request.form.get('year1'))
        year2 = int(request.form.get('year2'))

        n1 = date(year1, m1, dt1)
        n2 = date(year2, m2, dt2)

        difference = n2 - n1

        return render_template('index.html', difference=difference.days)
        
    return "Invalid Request", 400 

if __name__ == '__main__':
    app.run(debug=True)