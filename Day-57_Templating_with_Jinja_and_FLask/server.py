import datetime
import requests
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():
    current_date = datetime.datetime.now().year
    random_number = random.randint(1, 10)   # add imports in the server
    return render_template("index.html", num=random_number, year=current_date)  # now i can use it in the html file with jinja to use
                                                                                # imported commands via a kwarg (num is a variable kwarg)


@app.route('/guess/<name>')
def guess(name):
    age_json = requests.get(url=f"https://api.agify.io?name={name}")
    age_json.raise_for_status()
    data = age_json.json()
    age = data["age"]

    gender_json = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_json.raise_for_status()
    data_gender = gender_json.json()
    gender = data_gender["gender"]

    return render_template("guess.html", age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
