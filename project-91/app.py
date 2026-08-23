from flask import Flask, render_template, request

app = Flask(__name__)

# We handle both displaying the page (GET) and processing the form (POST) here
@app.route('/', methods=['GET', 'POST'])
def calculate():
    # If the user clicks the button to submit the form
    if request.method == 'POST' and 'input_string' in request.form:
        input_string = request.form.get('input_string', '')
        
        input_string = input_string.lower()
        number_of_vowels = 0    

        for i in input_string:
            if i in ['a', 'e', 'i', 'o', 'u']:
                number_of_vowels += 1

        # Return the template along with the calculated count
        return render_template('index.html', number_of_vowels=number_of_vowels)
        
    # FIX: If it is a normal GET request, just show the blank form
    return render_template('index.html', number_of_vowels=None)

if __name__ == '__main__':
    app.run(debug=True)
