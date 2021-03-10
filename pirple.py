from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "jaytatum" and password == "boston":
            message = model.show_color("jaytatum")
            return render_template("football.html", message=message)
        else:
            error_message = "Hint: He curses a lot"
            return render_template("index.html", message=error_message)
   
@app.route("/football", methods=['GET'])
def football():
    return render_template("football.html")

if __name__ == "__main__":
    app.run(debug=True)