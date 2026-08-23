from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    bmi = ""  # Initialized as empty string for clean GET requests
    
    if (
        request.method == "POST"
        and "Weight" in request.form
        and "Height" in request.form
    ):
        # Explicitly extracting matching case-sensitive keys
        weight = float(request.form.get("Weight"))  
        height = float(request.form.get("Height"))  
        
        # Proper metric BMI calculation formula
        bmi = round(weight / ((height / 100) ** 2), 2)  

    return render_template("index.html", bmi=bmi)

if __name__ == "__main__":
    app.run(debug=True)
