from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")  # Ensure this file exists in the templates folder
    
# Sign-Up route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("sign-up.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Fetch the submitted username and password
        username = request.form.get("username")
        password = request.form.get("password")

        # Add your authentication logic here
        if username == "admin" and password == "password":  # Example only
            return "Login Successful!"
        else:
            return "Invalid Credentials. Please try again."

    return render_template("login.html")  # Ensure login.html exists in the templates folder

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
