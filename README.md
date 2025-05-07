# 🌱 Agri Project – Agriculture Information Hub

This is a web application built using **Flask** that provides an Agriculture Information Hub. Users can sign up, log in, and search for crop-related information.

## 🚀 Features

- Home page with navigation
- About page describing the platform
- Crop Search interface
- Login & Signup functionality
- User-friendly design with Flask backend

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap (or your preferred styling)
- **Backend**: Python, Flask
- **WSGI Server**: Waitress (recommended for Windows)
- **Version Control**: Git & GitHub

## 🖥️ Project Structure

agri_project/
├── backend/
│ └── app.py # Flask app logic
├── templates/
│ ├── index.html
│ ├── about.html
│ ├── crop_search.html
│ ├── login.html
│ └── signup.html
├── static/
│ └── [your CSS/JS/images]
├── venv/ # Python virtual environment (not tracked)
├── .gitignore
└── README.md


## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/abhivarma2004/agri_project.git
cd agri_project
2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate    # Windows
3. Install Dependencies

pip install -r requirements.txt
4. Run the Application (Development)

python backend/app.py
Or for production using Waitress:


pip install waitress
python backend/app.py
The app will be available at: http://127.0.0.1:5000

📦 Requirements
Create a requirements.txt:
Flask
waitress
