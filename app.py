from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", name="Shama")
@app.route("/about")
def about():
    return render_template("about.html", about_info="contact me at ahsan@example.com")
@app.route("/contact")
def contact():
    return render_template("contact.html", contact_info="contact me at ahsan@example.com")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)