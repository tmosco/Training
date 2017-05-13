from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def home():
    username = request.args.get("username")
    return render_template("index.html", username=username)


@app.route("/if")
def home_two():
    username = request.args.get("username")
    if not username:
        return render_template("index2.html", username="World")
    else:
        return render_template("index2.html", username=username)


@app.route("/f")
def home_five():
    username = request.args.get("username")
    surname = request.args.get("surname")
    
    if username and surname:
        total = "{} {}".format(username, surname)
    elif surname and not username:
        total = surname
    elif username and not surname:
        total= username
    else:
        total = "World"
    return render_template("index2.html", username= total)

@app.route("/j")
def home_three():
    username = request.args.get("username")
    if username == None:
        username = "World"
    return render_template("index2.html", username=username)



@app.route("/g")
def home_four():
    username = request.args.get("username")
    if username != None:
        return render_template("index2.html", username=username)
    else:
        username="World"
if __name__ == "__main__":
    app.run(debug=True)
