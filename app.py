from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.run(port='80')
