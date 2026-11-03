from flask import Flask,render_template
import requests
post_data= requests.get(url='https://api.npoint.io/e4a2cf3481bfc9d4ba36').json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',posts=post_data)

@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/contact')
def contact():
        return render_template('contact.html')

@app.route('/post/<int:number>')
def see_post(number):
    req_post = None
    for posts in post_data:
        if posts['id'] == number:
            req_post = posts
    return render_template('post.html',post = req_post)

            


if __name__ == "__main__" :
    app.run(debug=1)