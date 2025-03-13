from flask import Flask, render_template, redirect, session, url_for
from authlib.integrations.flask_client import OAuth
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Google OAuth Config
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
LINKEDIN_CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
LINKEDIN_REDIRECT_URI = "http://localhost:5000/linkedin/callback"

oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    api_base_url="https://www.googleapis.com/oauth2/v3/", 
    access_token_url="https://oauth2.googleapis.com/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    userinfo_endpoint="https://www.googleapis.com/oauth2/v3/userinfo",
    client_kwargs={"scope": "openid email profile"},
    jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
)

linkedin = oauth.register(
    name="linkedin",
    client_id=LINKEDIN_CLIENT_ID,
    client_secret=LINKEDIN_CLIENT_SECRET,
    access_token_url="https://www.linkedin.com/oauth/v2/accessToken",
    authorize_url="https://www.linkedin.com/oauth/v2/authorization",
    api_base_url="https://api.linkedin.com/v2/",
    userinfo_endpoint="https://api.linkedin.com/v2/me",
    client_kwargs={"scope": "r_liteprofile r_emailaddress w_member_social"},
)

@app.route('/')
def home():
    user = session.get("user")
    return render_template('index.html', user=user)

@app.route("/google/login")
def google_login():
    return google.authorize_redirect(url_for("google_callback", _external=True))

@app.route("/google/callback")
def google_callback():
    token = google.authorize_access_token()
    user_info = google.get("userinfo").json()
    session["user"] = user_info
    return redirect(url_for("user_dashboard", username=user_info["name"]))

@app.route("/linkedin/login")
def linkedin_login():
    return linkedin.authorize_redirect(url_for("linkedin_callback", _external=True))

@app.route("/linkedin/callback")
def linkedin_callback():
    token = linkedin.authorize_access_token()
    user_info = linkedin.get("userinfo_endpoint").json()
    session["user"] = user_info
    return redirect(url_for("user_dashboard", username=user_info["localizedFirstName"]))

@app.route("/dashboard/<username>")
def user_dashboard(username):
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    
    return render_template("dashboard.html", user=user)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)