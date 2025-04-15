from flask import Flask, render_template, request, redirect, make_response
import base64
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/robots.txt')
def robots():
    return render_template("robots.html")

@app.route('/employee-login', methods=['GET', 'POST'])
def employee_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'kazim' and password == 'kazim123':
            session_data = {'user': 'kazim'}
            resp = make_response(redirect('/dashboard'))
            resp.set_cookie('session', base64.b64encode(json.dumps(session_data).encode()).decode())
            resp.set_cookie('admin', 'false')
            return resp
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html", error=None)

# @app.route('/dashboard')
# def dashboard():
#     session_cookie = request.cookies.get('session')
#     admin_cookie = request.cookies.get('admin')

#     try:
#         session_data = json.loads(base64.b64decode(session_cookie))
#         username = session_data.get('user', 'Guest')
#         is_admin = admin_cookie == 'true'
#         if is_admin:
#             return f"<h1>Welcome admin</h1><p>Authentication Bypassed</p>"
#         return f"<h1>Welcome {username}</h1>"
#     except:
#         return "Invalid session", 400

@app.route('/dashboard')
def dashboard():
    session_cookie = request.cookies.get('session')
    admin_cookie = request.cookies.get('admin')

    try:
        session_data = json.loads(base64.b64decode(session_cookie))
        username = session_data.get('user', 'Guest')
        is_admin = admin_cookie == 'true'
        return render_template('dashboard.html', username=username, is_admin=is_admin)
    except:
        return "Invalid session", 400


if __name__ == "__main__":
    app.run(debug=True)
