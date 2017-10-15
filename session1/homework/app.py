from flask import Flask, render_template,redirect,url_for,request,abort
app = Flask(__name__)

#binding
@app.route('/') #homepage
def index():
    return render_template("index.html")

@app.route('/school')
def school():
   return redirect("http://techkids.vn/", code=302, Response=None)

@app.route('/tuananh')
def tuananh():
    return "Hi Boss"

@app.route('/bmi/<int:weigh>/<float:high>')
def bmi(weigh,high):
    bmi = weigh/(high*high)
    if  bmi < 16:
        result = "Severely underweight"
    elif bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return "With BMI = " + str(int(bmi)) + " then you are " + result

if __name__ == '__main__':
  app.run(debug=True)
