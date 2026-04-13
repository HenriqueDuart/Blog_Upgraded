from flask import Flask, render_template, request
import requests
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

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

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        # Email details
        email_sender = 'henrique.ribeiroduarte@gmail.com'
        email_password = os.getenv("MAIL_PW")
        email_receiver = ['henrique.ribeiroduarte@gmail.com']
        port = 587

        subject = "New contact request"
        content = request.form["body"]
        final_content = content + '\n\n' + request.form["name"] + '\n' + request.form["email"] + '\n' + request.form[
            "phone"]

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg.set_content(final_content)

        with smtplib.SMTP('smtp.gmail.com', port=port) as connection:
            connection.starttls()
            connection.login(user=email_sender, password=email_password)
            connection.send_message(msg=msg)
            print('Email sent successfully.')

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