from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def show_application_form():
    """Show job application form for user input."""

    return render_template("/application-form.html")


@app.route("/application", methods=["POST"])
def show_application_response():
    """Returns response that acknowledges submission of job application form."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_requirement = request.form.get("salaryrequirement")
    desired_position = request.form.get("jobposition")

    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           job_title=desired_position,
                           salary=salary_requirement)


if __name__ == "__main__":
    app.run(debug=True)
