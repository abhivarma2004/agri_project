from flask import Flask, render_template, request, redirect, url_for, flash
from waitress import serve

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Secret key for session management

# Dummy data for login and signup
users = {
    "user@example.com": {"password": "password123"}
}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/crop_search')
def crop_search():
    return render_template('crop_search.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user exists in the dummy data
        if email in users and users[email]['password'] == password:
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid login credentials. Please try again.", "danger")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the email already exists
        if email in users:
            flash("This email is already registered.", "danger")
        else:
            users[email] = {"password": password}
            flash("Signup successful! Please log in.", "success")
            return redirect(url_for('login'))
    return render_template('signup.html')


# Run using Waitress (recommended for Windows)
if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5000)
