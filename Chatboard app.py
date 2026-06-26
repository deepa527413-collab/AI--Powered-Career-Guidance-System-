@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    answer = ""

    if request.method == "POST":

        question = request.form["question"].lower()

        if "python" in question:
            answer = "Python is widely used in AI, Data Science, Web Development, and Automation."

        elif "data science" in question:
            answer = "Learn Python, SQL, Statistics, Machine Learning, and Power BI."

        elif "ai" in question:
            answer = "AI Engineer is one of the fastest-growing careers. Learn Python, Machine Learning, and Deep Learning."

        else:
            answer = "Please ask a career-related question."

    return render_template("chatbot.html", answer=answer)
