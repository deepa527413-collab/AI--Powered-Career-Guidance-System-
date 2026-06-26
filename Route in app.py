@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT name,email FROM users WHERE email=%s",
        (session["user"],)
    )

    data = cur.fetchone()
    cur.close()

    user = {
        "name": data[0],
        "email": data[1],
        "interest": "Artificial Intelligence",
        "skills": "Python, SQL"
    }

    return render_template("profile.html", user=user)
