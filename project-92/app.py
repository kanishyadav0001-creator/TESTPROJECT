from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display UI 1 (Form)
@app.route('/')
def home():
    return render_template('form.html')

# Route to process data and display UI 2 (Resume)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get data from the form inputs
        dob = request.form.get('dob')
        father_name = request.form.get('father_name')
        mother_name = request.form.get('mother_name')
        hobbies = request.form.get('hobbies')
        
        # Pass the data to the resume template
        return render_template('resume.html', dob=dob, father_name=father_name, mother_name=mother_name, hobbies=hobbies)

if __name__ == '__main__':
    app.run(debug=True)