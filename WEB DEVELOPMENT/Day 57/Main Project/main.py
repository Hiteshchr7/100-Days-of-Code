from flask import Flask, render_template
from post import Post
import requests
app = Flask(__name__)
posts =  requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

all_posts = [Post(post["id"],post["title"],post["subtitle"],post["body"]) for post in posts]
@app.route('/')
def home():
    return render_template("index.html", all_posts = all_posts)

@app.route("/post/<int:num>")
def view_post(num):
    return render_template("post.html",post= all_posts[num-1])
if __name__ == "__main__":
    app.run(debug=True)
