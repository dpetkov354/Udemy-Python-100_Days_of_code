from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = "INSERT E-MAIL"
OWN_PASSWORD = "INSERT PASSWORD"

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


@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
