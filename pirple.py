from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "username" and password == "password":
            return render_template("index.html", message="You're signed in")
        else:
            error_message = "Hint: He curses a lot"
            return render_template("index.html", message=error_message)
   
@app.route("/football", methods=['GET'])
def football():
    return render_template("football.html")

if __name__ == "__main__":
    app.run(debug=True)