from flask import Flask, render_template
import datetime

app = Flask(__name__)
fish = datetime.datetime.now()
sus = fish.strftime("%Y")
print(sus)
@app.route('/')
def hello():
    return render_template("article.html", mim=sus)

if __name__ == "__main__":
    app.run(debug=True)