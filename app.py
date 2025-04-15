from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/robots.txt')
def robots():
    return render_template("robots.html")

if __name__ == "__main__":
    app.run(debug=True)