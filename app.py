import os
import logging
from flask import Flask, render_template, request, url_for, redirect, jsonify
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
from flask_sqlalchemy import SQLAlchemy
import json

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config.from_object(onfig.ProductionConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Project

@app.route("/sendemail/", methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        your_name = "Venu Gopala Krishna Gieraboni"
        your_email = "vgkrishna117@gmail.com"
        your_password = "gopikrishna117@vgk"

        # Logging in to our email account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(your_email, your_password)

        # Sender's and Receiver's email address
        sender_email = "vgkrishna117@gmail.com"
        receiver_email = "vgieraboni@leomail.tamuc.edu"

        msg = EmailMessage()
        msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
        msg['Subject'] = 'New Response on Personal Website'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
        except:
            pass
    return redirect('/');

@app.route("/add/project", methods=['POST'])
def add_project():
    name = request.form['name']
    role = request.form['role']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    description = request.form['description']

    # name = request.args.get('name')
    # role = request.args.get('role')
    # start_date = request.args.get('start_date')
    # end_date = request.args.get('end_date')
    # description = request.args.get('description')
    try:
        project = Project(
            name = name,
            role = role,
            start_date = start_date,
            end_date = end_date,
            description = description
        )
        app.logger.info("Project Details: {}".format(project))
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route("/")
@app.route("/home")
def index():
    try:
        projects=Project.query.all()
        return render_template("index.html", projects = projects)
    except Exception as e:
	    return(str(e))
    

if __name__ == "__main__":
    app.run(debug=True)