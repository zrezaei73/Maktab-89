from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('create_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    if len(password) < 8:
        error = 'password must be at least 8 characters long!'
    elif password != password_confirmation:
        error = 'password does not match!!'
    else:
        create_user()
        return 'user created successfully!!!'
    return render_template('create_user.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

