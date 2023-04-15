from flask import Flask,render_template,request,session,redirect,url_for


app = Flask(__name__)

app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)