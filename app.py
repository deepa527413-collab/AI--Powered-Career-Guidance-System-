from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "career_guidance_secret"

# MySQL Configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "career_guidance"

mysql = MySQL(app)

# Home
@app.route("/")
def home():
    return render_template("index.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
            (name, email, password)
        )
        mysql.connection.commit()
        cur.close()

        flash("Registration Successful")
        return redirect(url_for("login"))

    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cur.fetchone()
        cur.close()

        if user:
            session["user"] = email
            return redirect(url_for("dashboard"))

        flash("Invalid Login")

    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# Career Recommendation
@app.route("/career", methods=["GET", "POST"])
def career():
    recommendation = ""

    if request.method == "POST":
        skills = request.form["skills"].lower()

        if "python" in skills:
            recommendation = "Data Scientist / AI Engineer"
        elif "java" in skills:
            recommendation = "Java Developer"
        elif "html" in skills:
            recommendation = "Frontend Developer"
        elif "sql" in skills:
            recommendation = "Database Administrator"
        else:
            recommendation = "Software Engineer"

    return render_template(
        "career.html",
        recommendation=recommendation
    )

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
