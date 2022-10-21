from datetime import datetime
from venv import create
from src import app, db, bcrypt
from flask import render_template, request, url_for, flash, jsonify, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
# Login route
def login():
    data = request.form
    if request.method == "POST":
        try:
            if user := User.query.filter_by(username=data['username']).first():
                if bcrypt.check_password_hash(user.password, data['password']):
                    print(user.password)
                    print(login_user(user))
                    return redirect(url_for('dashboard'))

                else:
                    return flash("Mot de passe invalide")
            else:
                flash("Nom d'utilisateur ou mot de passe invalide")
        except Exception:
            flash("Nom d'utilisateur ou mot de passe invalide")
    return render_template('auth/login.html')


@app.route('/register', methods=['GET', 'POST'])
# Register route
def register():
    if request.method == "POST":
        data = request.form
        hashed_password = bcrypt.generate_password_hash(data['password'])
        try:
            new_user = User(
                username=data['username'],
                email=data['email'],
                password=hashed_password,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': "Votre compte a bien été créé"})
        except Exception:
            return jsonify({'message': "Nom d'utilisateur ou adresse email existant"})
    return render_template("auth/register.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    data = [i.get_data() for i in users]
    return jsonify({'data': data})


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('index.html', name=current_user.username)
