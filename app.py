from textblob import TextBlob
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("user_input") # request from flask gets the submitted input (Flask for GET)
        print(text)
        r = TextBlob(text).sentiment
        return render_template("index.html", result = r) # return the HTML template back to you
    else: # means havent pressed enter yet.
        return render_template("index.html", result = "waiting ...")

if __name__ == "__main__":
    app.run()
