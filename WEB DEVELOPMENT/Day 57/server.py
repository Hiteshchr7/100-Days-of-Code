from flask import Flask,render_template
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def home():
    year = dt.datetime.now().year
    return render_template("index.html",ima=year)

@app.route("/guess/<name>")
def api_use(name):
    url1 = "https://api.genderize.io"
    url2 = "https://api.agify.io"
    param = {
    "name" : f"{name}"
    }
    age = requests.get(url2,params=param).json()["age"]
    gender = requests.get(url1,params=param).json()["gender"]
    return render_template("guess.html",name=param["name"],age=age,gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts =  requests.get(blog_url).json()
    return render_template("blog.html",posts=all_posts)
if __name__ =="__main__" :
    app.run(debug=True)