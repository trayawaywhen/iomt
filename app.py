from graphs import graph
from mqtt_subscribe import get_rpi_data

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash

##############################
# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hsgfd7sdfgbjsdf56dsf89adsgdfbjgh5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Residents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    
# Create database
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##############################
# Routes
@app.route('/')
@login_required
def index():
    residents = Residents.query.all()
    return render_template('index.html', residents = residents)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if a user already exists
        existing_user = User.query.first()
        if existing_user:
            flash('A user already exists. Signup is not allowed.', 'danger')
            return redirect(url_for('login'))

        # Create the new admin user
        # hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=password, is_admin=True)
        db.session.add(new_user)
        db.session.commit()
        flash('Signup successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Use hashed passwords in production
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    residents = Residents.query.all()
    if not current_user.is_admin:
        return "Access Denied", 403
    return render_template('admin.html', residents = residents)

@app.route('/add_user', methods=['POST'])
@login_required
def add_user():
    if not current_user.is_admin:
        return "Access Denied", 403
    username = request.form['username']
    password = request.form['password']
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    flash('User added successfully!')
    return redirect(url_for('admin'))

@app.route('/dashboard')
@login_required
def dashboard():
    residents = Residents.query.all()
    if not current_user.is_admin:
        return "Access Denied", 403
    data = graph()
    return render_template('dashboard.html', data = data, residents = residents)

@app.route('/residents')
@login_required
def persons():
    residents = Residents.query.all()
    if not current_user.is_admin:
        return "Access Denied", 403
    return render_template('residents.html', residents = residents)

@app.route('/add_resident', methods=['POST'])
@login_required
def add_resident():
    if request.method == 'POST':
        username = request.form['username']
        new_resident = Residents(username=username)
        db.session.add(new_resident)
        db.session.commit()
        flash('Resident added successfully!', 'success')
        return redirect(url_for('admin'))
    return render_template('admin.html')

@app.route('/resident/<int:user_id>')
def resident_profile(user_id):
    resident = Residents.query.get_or_404(user_id)  # Fetch the user or return a 404 if not found
    residents = Residents.query.all()
    return render_template('resident_profile.html', resident=resident, residents = residents)



##############################
# Run
if __name__ == '__main__':
    app.run(host='0.0.0.0')