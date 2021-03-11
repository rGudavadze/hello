from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = 'jumpjacks'

username = ''
user = model.check_users()


@app.route("/", methods=['GET'])
def home():
    if 'username' in session:
        g.user = session['username']
        return render_template('football.html', message="<img src='static/img/unnamed.png'>")
    return render_template('homepage.html', message="Log in or sign up!")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop("username", None)
        areyouuser = request.form.get('username')
        pwd = model.check_pw(areyouuser)
        if request.form.get('password') == pwd:
            session['username'] = request.form.get('username')
            return redirect(url_for('home'))
    
    return render_template('index.html')

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        message = "Please sign up!"
        return render_template("signup.html", message=message)
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        fav_color = request.form.get("fav_color")
        message = model.signup(username, password, fav_color)
        return render_template('signup.html', message=message)

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)