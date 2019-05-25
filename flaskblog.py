from flask import Flask,render_template,url_for
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
def hello():
    return render_template("home.html",post=posts,title="HOME")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    

if __name__=='__main__':
    app.run(debug=True)