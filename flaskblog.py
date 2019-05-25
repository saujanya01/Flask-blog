from flask import Flask,render_template,url_for,flash, redirect
from forms import RegistrationForm, LoginForm

app=Flask(__name__)
app.config['SECRET_KEY']='be90808bf89e7c74a63362f6e50914ff'

posts = [
    {
        "author":"Saujanya Tiwari",
        "title":"blog post 1",
        "content":"First Post Content",
        "date_posted":"April 20, 2018"
    },
    {
        "author":"XYZ",
        "title":"blog post 2",
        "content":"First Post Content",
        "date_posted":"April 21, 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",post=posts,title="HOME")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register",methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)