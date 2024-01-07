from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    req_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(req_url)
    res = response.json()
    return render_template("index.html", posts=res)

@app.route("/guess/<user_name>")
def guess(user_name):
    gender_predict = f'https://api.genderize.io/?name={user_name}'
    age_predict = f'https://api.agify.io/?name={user_name}'
    print(user_name)
    response = requests.get(gender_predict)
    print(response.json())
    res_gen = response.json()['gender']
    response = requests.get(age_predict)
    age_gen = response.json()['age']
    return render_template("guess.html", name=user_name, gen=res_gen, age=age_gen)

@app.route("/blog/<number>")
def get_blog(number):
    print(number)
    req_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(req_url)
    res = response.json()
    print(res)
    return render_template("blog.html", posts=res, number=int(number))


if __name__ == "__main__":
    app.run(debug=True)