
from flask import Flask , render_template , url_for
app = Flask(__name__)

posts = [
    {
        'author' : "Amr Ezz",
        'title' : "Post Number 1",
        'content' : 'Content 1 Content 1 Content 1 Content 1 Content 1 Content 1 Content 1 ',
        'date' : '20 April 2020'
    },
    {
        'author' : "Hany Adel",
        'title' : "Post Number 2",
        'content' : 'Content 2 Content 2 Content 2 Content 2 Content 2 Content 2 Content 2 ',
        'date' : '21 April 2020'
    }
]

@app.route('/')
def index():
    return render_template('/index.html',posts=posts)

@app.route('/about')
def about():
    return render_template('/about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)