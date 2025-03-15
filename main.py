from flask import Flask, render_template, redirect, session, url_for, request
from authlib.integrations.flask_client import OAuth
import os
from config import post_generation_template
from langchain_core.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
import requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Initialize Search Tool
search = DuckDuckGoSearchRun(name='Search')
tools = [Tool.from_function(name="search_news", func=search.run, description="Search for news articles.")]

# Initialize LLM
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama3-70b-8192")
prompt = PromptTemplate(
    input_variables=['user_input', 'writing_style'],
    template=post_generation_template,
    validate_template=True
)

generation_chain = prompt | llm 

# OAuth Config
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
    client_kwargs={"scope": "openid email w_member_social"},
    grant_type="authorization_code", 
    server_metadata_url=None, 
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
    return redirect(url_for("dashboard", username=user_info["name"]))

@app.route("/linkedin/login")
def linkedin_login():
    return linkedin.authorize_redirect(
        url_for("linkedin_callback", _external=True),
        response_type="code" 
    )

@app.route("/linkedin/callback")
def linkedin_callback():
    # Get authorization code
    auth_code = request.args.get("code")
    if not auth_code:
        return "Authorization code not found!", 400

    # Exchange authorization code for access token
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    redirect_uri = url_for("linkedin_callback", _external=True)
    
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "client_id": LINKEDIN_CLIENT_ID,
        "client_secret": LINKEDIN_CLIENT_SECRET,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=data, headers=headers)
    token_data = response.json()

    if "access_token" not in token_data:
        print(f"Token exchange error: {token_data}")
        return f"Failed to get access token: {token_data}", 400

    access_token = token_data["access_token"]
    session["linkedin_token"] = access_token
    
    # Step 3: Fetch User Profile Info
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info = requests.get("https://api.linkedin.com/v2/me", headers=headers).json()

    # Step 4: Fetch User Email
    email_info = requests.get(
        "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))",
        headers=headers
    ).json()

    user_id = user_info.get("id")
    first_name = user_info.get("localizedFirstName")
    last_name = user_info.get("localizedLastName")
    email = email_info["elements"][0]["handle~"]["emailAddress"] if "elements" in email_info else "Not Provided"

    # Step 5: Store User Details in Session
    session["user"] = {
        "id": user_id,
        "name": f"{first_name} {last_name}",
        "email": email
    }

    # Redirect User to Dashboard
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
@app.route("/dashboard/<username>")
def dashboard(username=None):
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

@app.route("/generate_post", methods=["POST"])
def generate_post():
    user_input = request.form.get("user_input")
    writing_style = request.form.get("writing_style")

    if not user_input:
        return "No input provided", 400

    # Generate post using LLM
    post = generation_chain.invoke({"user_input": user_input, "writing_style": writing_style})

    return render_template("dashboard.html", user=session["user"], post=post.content)

if __name__ == '__main__':
    app.run(debug=True)