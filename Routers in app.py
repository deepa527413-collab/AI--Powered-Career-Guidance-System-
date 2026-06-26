@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    message = ""

    if request.method == "POST":

        feedback = request.form["feedback"]

        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO feedback(user_email,feedback) VALUES(%s,%s)",
            (session["user"], feedback)
        )

        mysql.connection.commit()
        cur.close()

        message = "Thank you for your feedback."

    return render_template(
        "feedback.html",
        message=message
    )
