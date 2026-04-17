from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"   # required for session

@app.route("/", methods=["GET", "POST"])
def signup():
    error = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        if not name or not email or not phone or not password:
            error = "⚠️ All fields are required!"
        else:
            # store user data in session
            session["user"] = {
                "name": name,
                "email": email,
                "phone": phone
            }
            return redirect(url_for("dashboard"))

    return render_template("signup.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("signup"))

    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.pop("user", None)   # clear session
    return redirect(url_for("signup"))


if __name__ == "__main__":
    app.run(debug=True)