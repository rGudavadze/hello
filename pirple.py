from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("structure.html")
   
@app.route("/football", methods=['GET'])
def football():
    return render_template("football.html")

if __name__ == "__main__":
    app.run(debug=True)