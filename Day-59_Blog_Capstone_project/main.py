from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/5808b1a3304a496f4c65").json() ##### add the posts data link

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html", all_posts=posts)    ##### add the posts data


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/<int:index>")  # generate blog number
def show_post(index):
    requested_post = None
    for blog_post in posts:    # get the correct id to index data
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
