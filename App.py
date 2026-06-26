import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/resume", methods=["GET", "POST"])
def resume():

    message = ""

    if request.method == "POST":

        file = request.files["resume"]

        if file:

            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            message = "Resume uploaded successfully!"

    return render_template("resume.html", message=message)
