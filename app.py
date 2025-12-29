from flask import Flask, render_template, request
from Model import init_db, add_user, check_user, user_exists

app = Flask(__name__)
app.secret_key = "secret123"

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if user_exists(username):
        return render_template(
            'index.html',
            message="Username already exists. Please login."
        )

    success = add_user(username, password)
    if success:
        return render_template(
            'login.html',
            message="Registration successful. Please login."
        )
    else:
        return render_template(
            'index.html',
            message="Registration failed. Try again."
        )

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if check_user(username, password):
        return render_template(
            'login.html',
            message="Login successful!"
        )
    else:
        return render_template(
            'index.html',
            message="Invalid username or password."
        )

@app.route('/login-page')
def login_page():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
