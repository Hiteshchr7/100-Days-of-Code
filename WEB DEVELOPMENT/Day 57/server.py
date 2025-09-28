from flask import Flask,render_template
import datetime as dt
import requests

url1 = "https://api.genderize.io"
url2 = "https://api.agify.io"
app = Flask(__name__)
@app.route("/guess/<name>")
def api_use(name):
    param = {
    "name" : f"{name}"
}
    age = requests.get(url2,params=param).json()["age"]
    gender = requests.get(url1,params=param).json()["gender"]
    return render_template("guess.html",name=param["name"],age=age,gender=gender)

@app.route("/")
def home():
    year = dt.datetime.now().year
    return render_template("index.html",ima=year)

if __name__ =="__main__" :
    app.run(debug=True)