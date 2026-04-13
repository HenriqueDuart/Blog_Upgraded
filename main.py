from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url="https://api.npoint.io/309d02e5bb7e6bd448e4"
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", all_posts=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/posts/<id>')
def posts(id):
    url = "https://api.npoint.io/309d02e5bb7e6bd448e4"
    response = requests.get(url=url)
    response.raise_for_status()
    all_data = response.json()
    filtered_data = all_data[int(id)-1]
    return render_template("post.html", post_content=filtered_data)

if __name__=="__main__":
    app.run(debug=True)