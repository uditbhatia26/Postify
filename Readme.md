# 🚀 **Postify - AI-Powered Content Automation & Authentication**

## 📌 **Project Overview**

Postify is an **AI-powered content automation tool** designed to streamline content creation, editing, and posting. Users can **log in via Google or LinkedIn OAuth**, generate AI-powered posts, preview & edit them, and post them directly to LinkedIn—all from a **single dashboard**.

---

## 🔧 **Features**

### 1️⃣ **AI-Powered Content Generation**

✅ **Predefined Writing Styles** – Choose from **Professional, Storytelling, or Casual** tones.  
✅ **Custom Writing Style** – Define your own tone (e.g., _“Write like Elon Musk”_).  
✅ **News-Based Post Creation** – Fetches **real-time news** to generate relevant content.  
✅ **RAG-Based Post Generation** (Upcoming) – Generate **insightful LinkedIn posts from PDFs of research papers**.

### 2️⃣ **Live Editing & Preview**

✅ **Instant AI-Generated Drafts** – Get **multiple variations** of your post.  
✅ **Real-Time Editing** – Modify the AI-generated content to **match your voice**.  
✅ **Post Preview Panel** – See exactly how your LinkedIn post will appear **before posting**.  
✅ **Image Upload & Preview** – Upload **custom images** and see them in the **preview section**.

### 3️⃣ **One-Click Auto-Posting to LinkedIn**

✅ **Seamless API Integration** – Post **directly to LinkedIn** with **one click**.  
✅ **Post Scheduling** (Upcoming) – Schedule posts for **future publishing**.  
✅ **User Mentions in Posts** (Upcoming) – Mention **LinkedIn connections** in your posts.  
✅ **Hashtag & SEO Optimization** – AI suggests **trending hashtags** for better reach.

### 4️⃣ **User Authentication & Dashboard**

✅ **User Authentication:** Secure **Google & LinkedIn OAuth login**.  
✅ **Personalized Dashboard:** Each user gets a **unique dashboard**.  
✅ **Secure Session Management:** Stores user sessions **securely**.  
✅ **Custom Authentication Page:** Users can log in via **email/password or social login**.  
✅ **Responsive UI:** Modern UI for a **seamless experience**.

---

## 🛠️ **Tech Stack**

| **Category**               | **Technology Used**                     |
| -------------------------- | --------------------------------------- |
| **Backend**                | Flask (Python)                          |
| **AI Model**               | LangChain (LLM-powered text generation) |
| **Authentication**         | Google OAuth, LinkedIn OAuth (Authlib)  |
| **Search Integration**     | Serper API (Google Search)              |
| **Database**               | SQLite (Optional, for user storage)     |
| **Frontend**               | HTML, CSS (Jinja2 Templates)            |
| **Environment Management** | `dotenv` for secure credential handling |

---

## 🚀 **Getting Started**

### **1️⃣ Clone the Repository**

````bash
git clone https://github.com/yourusername/postify.git
cd postify

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
````

### 3️⃣ Set Up Environment Variables

Create a `.env` file and add the following:

```ini
GOOGLE_CLIENT_ID="your_google_client_id"
GOOGLE_CLIENT_SECRET="your_google_client_secret"
LINKEDIN_CLIENT_ID="your_linkedin_client_id"
LINKEDIN_CLIENT_SECRET="your_linkedin_client_secret"
GROQ_API_KEY="your_secret_key"
SERPER_API_KEY="your_serper_api_key"
SECRET_KEY="your_flask_secret_key"
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
│── static/  # CSS, JS, and assets
│── main.py  # Flask application
│── config.py  # Configuration settings
│── requirements.txt  # Dependencies
│── .env  # Environment variables (Not to be committed)
│── README.md  # Project documentation
```

## ✨ Future Enhancements

- ✔️ Image Upload & Preview in Posts (📸 In Progress)
- ✔️ Real-Time Web Search Integration (Serper API and DDG)
- ✔️ Post Scheduling for Later Publishing
- ✔️ User Mentions in LinkedIn Posts (@Name Feature)
- ✔️ RAG-Based Post Generation from PDFs (Research Papers)
- ✔️ Multi-Platform Posting (Twitter/X, Medium, Facebook)
- ✔️ Post Analytics & Performance Tracking
