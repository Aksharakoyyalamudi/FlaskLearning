from flask import Blueprint, redirect,render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('here')
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, signup_details['param1'], password, signup_details['param2'])
        if email == signup_details['param1'] and password == signup_details['param2']:
            flash('account created', category="success")
            return redirect("/classes")
    return render_template("login.html")

@auth.route('/classes')
def classes():
    return render_template("classes.html")

signup_details = {}
@auth.route('/sign-up',  methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        signup_details['param1']=email
        signup_details['param2']=password
        print(signup_details)
        return redirect("/login")
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     first_name = request.form.get('firstName')
    #     password1 = request.form.get('password1')
    #     password2 = request.form.get('password2')
        
    #     if len(email) < 4:
    #         flash('Email must be greater than 3 characters.', category='error')
    #     elif len(first_name) < 2:
    #         flash('First name must be greater than 1 character.', category='error')
    #     elif password1 != password2:
    #         flash('Passwords don\'t match.', category='error')
    #     elif len(password1) < 7:
    #         flash('Password must be at least 7 characters.', category='error')
    #     else:
    #         flash('account created', category="success")

    return render_template("Register.html")