
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    fname=request.form['fname']
    age=request.form['age']
    return render_template('greeting.html', fname=fname, age=age)
if(__name__=="__main__"):
    app.run( host='0.0.0.0', port=5000, debug=True)