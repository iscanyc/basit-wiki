from flask import Flask, render_template, request
from requests import get

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        q = request.form["word"]
        data = get("https://tr.wikipedia.org/w/rest.php/v1/search/page?q={}&limit=100".format(q)).json()
        return render_template("query.html", data=data, title=q)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(host='localhost')
