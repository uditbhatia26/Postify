# 🚀 Postify - AI-Powered Content Automation & Authentication

## 📌 Project Overview

Postify is an **AI-powered content automation tool** that streamlines content creation and posting. It allows users to **sign up and log in using Google or LinkedIn OAuth authentication**, ensuring a seamless and secure experience. Users get personalized dashboards and can manage their content effortlessly.

## 🔧 Features

### 1️⃣ AI-Powered Content Generation

✅ **Predefined Writing Styles** – Choose from **Professional, Storytelling, or Casual** tones.  
✅ **Custom Writing Style** – Define your own tone (e.g., “Write like Elon Musk”).  
✅ **News-Based Post Creation** – Fetches **real-time news** to generate relevant content.

### 2️⃣ Live Editing & Preview

✅ **Instant AI-Generated Drafts** – Get **multiple variations** of your post.  
✅ **Edit & Customize** – Fine-tune the content to **match your voice**.

### 3️⃣ One-Click Auto-Posting to LinkedIn

✅ **Seamless API Integration** – Post **directly to LinkedIn** with **one click**.  
✅ **Post Scheduling** – Schedule posts for **later**.  
✅ **Hashtag & SEO Optimization** – AI suggests **trending hashtags** for better reach.

### 4️⃣ User Authentication & Dashboard

✅ **User Authentication:** Login/Signup using **Google & LinkedIn OAuth**.  
✅ **Personalized Dashboard:** Each registered user gets a **unique dashboard page**.  
✅ **Secure Session Management:** Stores user data securely during the session.  
✅ **Custom Authentication Page:** Users can log in via **email/password or social login**.  
✅ **Responsive UI:** Styled HTML templates for a smooth experience.

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Authentication:** Google OAuth, LinkedIn OAuth (via Authlib)
- **Database:** SQLite (Optional for user storage)
- **Frontend:** HTML, CSS (Templated with Jinja2)
- **Environment Management:** `dotenv` for secure credential handling

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
  git clone https://github.com/yourusername/postify.git
  cd postify
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file and add the following:

```ini
GOOGLE_CLIENT_ID="your_google_client_id"
GOOGLE_CLIENT_SECRET="your_google_client_secret"
LINKEDIN_CLIENT_ID="your_linkedin_client_id"
LINKEDIN_CLIENT_SECRET="your_linkedin_client_secret"
SECRET_KEY="your_secret_key"
```

### 4️⃣ Run the Flask App

```bash
python main.py
```

### 5️⃣ Access the App

Go to `http://localhost:5000/` in your browser.

## 📂 Project Structure

```
postify/
│── templates/
│   ├── index.html  # Homepage with login options
│   ├── login.html  # Login page with social authentication
│   ├── dashboard.html  # User dashboard
│── main.py  # Flask application
│── requirements.txt  # Dependencies
│── .env  # Environment variables (Not to be committed)
│── README.md  # Project documentation
```

## ✨ Future Enhancements

- ✅ Store user data persistently in a database (PostgreSQL or Firebase)
- ✅ Allow users to customize their profiles
- ✅ Multi-platform integration (Twitter, Medium, etc.)
