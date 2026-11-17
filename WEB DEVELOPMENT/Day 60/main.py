from flask import Flask, render_template,request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("my_email")
my_password = os.getenv("my_password")
smtp_add = os.getenv("smtp_address")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['POST','GET'])
def contact():
    if request.method=='POST' :
        data = request.form

        with smtplib.SMTP(smtp_add,port=587) as connection :
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject: NEW MESSAGE! \n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}".encode("utf-8"))
            
        return render_template("contact.html",msg_sent=1)
    return render_template("contact.html",msg_sent=0)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
