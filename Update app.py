from ai_engine import recommend_career

@app.route("/career", methods=["GET", "POST"])
def career():

    result = None

    if request.method == "POST":

        skills = request.form["skills"]

        result = recommend_career(skills)

    return render_template(
        "career.html",
        result=result
    )
