from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def get_data():
    name = request.form['username']
    pasw = request.form['password']
    return f"<h1>Name:{name},Password:{pasw}</h1>"

if __name__ == '__main__':
    app.run(debug=1)